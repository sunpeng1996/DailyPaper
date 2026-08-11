---
title: 'WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration
  and Security in Human-Centered Agent Networks'
title_zh: WeClawArena：以人为中心代理网络跨用户协作安全的可审计基准
authors:
- Prince Zizhuang Wang
- Aojie Yuan
- Haiyue Zhang
- Xiyang Hu
- Yue Zhao
- Shuli Jiang
affiliations:
- Carnegie Mellon University
- University of Southern California
- Arizona State University
arxiv_id: '2608.03499'
url: https://arxiv.org/abs/2608.03499
pdf_url: https://arxiv.org/pdf/2608.03499
published: '2026-08-03'
collected: '2026-08-11'
category: Agent
direction: 多Agent跨用户协作安全评测
tags:
- Multi-Agent
- Benchmark
- Security
- Audit
- Workspace Collaboration
one_liner: 首个支持跨用户私有工作空间协作、可审计攻击路径的多代理评测基准与运行沙箱
practical_value: '- 做电商多代理协作场景（如商家代理、平台代理、用户代理的议价/履约/审批流程）时，可复用四类危害（协作/安全/隐私/治理）的攻击设计框架，提前模拟业务风险

  - 「任务效用与攻击成功率分离评估」的方法可直接迁移到业务系统评测，避免只看任务完成率忽略隐私泄露、越权操作等隐性风险，尤其适配电商交易、广告投放等高合规要求场景

  - Docker隔离用户工作空间+网关统一审计的工程架构，可复用在企业多代理系统的安全管控模块，自动留存全链路操作证据，满足合规审计要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
随着个人代理框架快速落地，以人为中心的代理网络中，多个用户的代理需要跨私有工作空间完成协作任务，但现有基准仅覆盖单用户工具调用或共享沙箱内的多代理交互，没有同时评估跨用户协作的任务完成率、攻击危害、可审计性三大核心问题，也缺乏真实的跨用户任务场景与攻击模拟体系。

### 方法关键点
- 覆盖议价、招投标、旅行、软件工程、临床、交易6个跨用户任务域，共124个基础任务，每个任务扩展为1个无攻击对照组+4类攻击（协作破坏/安全入侵/隐私泄露/治理越权）变体，合计620个评测场景。
- 沙箱基于Docker实现用户私有工作空间隔离，通过网关统一路由代理通信、工具调用、资源操作，自动留存全链路审计证据，包括消息、工具调用记录、资源变更、权限路径、最终工作空间状态。
- 评估体系分离任务成功率（TSR）与攻击成功率（ASR），ASR仅在存在明确攻击到最终危害的证据链时才判定为成功，避免误判。

### 关键实验
测试了8款主流闭源/开源LLM backbone：Claude Opus 4.7整体任务表现最优，旅行域TSR达83.0%，SWE域达34.0%；攻击抗性方面Claude Opus 4.7的1-ASR（攻击失败率）达97.4%，开源模型的攻击抗性普遍低于闭源模型，最低仅51.1%；任务成功率下降与攻击成功率无完全对齐关系，部分攻击不影响任务完成但会造成隐私泄露等隐性危害。

最值得记住的一句话：跨用户代理协作中，任务完成率不能替代安全评估，必须将私有工作空间边界管控、权限路径审计作为多代理系统上线的必要评估项。
