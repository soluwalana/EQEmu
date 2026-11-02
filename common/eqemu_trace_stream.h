#pragma once
// A proxy around the EQEmu lower stream. Capture packets *after* StructStrategy
// encoding but *before* transport framing/compression.
#include "common/eq_stream_intf.h"
#include "common/eq_packet_trace.h"
#include <memory>
#include <string>

namespace PacketTrace {

class StreamTap final : public EQStreamInterface {
public:
    explicit StreamTap(std::shared_ptr<EQStreamInterface> dest)
        : dest_(std::move(dest)) {}

    void QueuePacket(const EQApplicationPacket* p, bool ack_req = true) override {
        Record(p, true, true, dest_->GetRemoteAddr());
        dest_->QueuePacket(p, ack_req);
    }
    void FastQueuePacket(EQApplicationPacket** p, bool ack_req = true) override {
        if (p && *p) Record(*p, true, true, dest_->GetRemoteAddr());
        dest_->FastQueuePacket(p, ack_req);
    }
    EQApplicationPacket* PopPacket() override { return dest_->PopPacket(); }
    void Close() override { dest_->Close(); }
    void ReleaseFromUse() override { dest_->ReleaseFromUse(); }
    void RemoveData() override { dest_->RemoveData(); }
    std::string GetRemoteAddr() const override { return dest_->GetRemoteAddr(); }
    uint32 GetRemoteIP() const override { return dest_->GetRemoteIP(); }
    uint16 GetRemotePort() const override { return dest_->GetRemotePort(); }
    bool CheckState(EQStreamState s) override { return dest_->CheckState(s); }
    std::string Describe() const override { return dest_->Describe(); }
    void SetActive(bool val) override { dest_->SetActive(val); }
    MatchState CheckSignature(const Signature* s) override { return dest_->CheckSignature(s); }
    EQStreamState GetState() override { return dest_->GetState(); }
    void SetOpcodeManager(OpcodeManager** opm) override { dest_->SetOpcodeManager(opm); }
    OpcodeManager* GetOpcodeManager() const override { return dest_->GetOpcodeManager(); }
    const EQ::versions::ClientVersion ClientVersion() const override { return dest_->ClientVersion(); }
    Stats GetStats() const override { return dest_->GetStats(); }
    void ResetStats() override { dest_->ResetStats(); }
    EQStreamManagerInterface* GetManager() const override { return dest_->GetManager(); }

private:
    std::shared_ptr<EQStreamInterface> dest_;
};
} // namespace PacketTrace
