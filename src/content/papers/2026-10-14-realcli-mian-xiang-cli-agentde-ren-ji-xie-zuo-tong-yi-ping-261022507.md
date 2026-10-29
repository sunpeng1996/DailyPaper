---
title: 'RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI
  Agents'
title_zh: RealCLI：面向CLI Agent的人机协作统一评估基准
authors:
- Yunqi Liu
- Peiyu Wang
- Bingli Wang
- Leo Luo
- Xuanwu Song
- Xudong Ma
- Hongxin Li
- Yaxin Du
- Weicheng Gu
- Fanglin Xu
affiliations:
- Beihang University
- Renmin University
- IQuest Research
arxiv_id: '2610.22507'
url: https://arxiv.org/abs/2610.22507
pdf_url: https://arxiv.org/pdf/2610.22507
published: '2026-10-14'
collected: '2026-10-29'
category: Agent
direction: Agent 人机协作能力评估基准
tags:
- CLI Agent
- Human-Agent Collaboration
- Benchmark
- Agent Evaluation
- Long-Horizon Agent
one_liner: 构建了覆盖任务执行与5维协作质量的双模式CLI Agent统一评测基准
practical_value: '- 构建业务Agent（如电商运营自动化Agent、客服Agent）的评估体系时，可复用5维协作框架（可理解性/可操控性/观测恢复/信任校准/安全意识），避免仅考核任务完成率而忽略用户体验与合规风险。

  - 设计人机协作场景评测集时，可参考「信息分片渐进披露+交互探针」的方案，模拟真实用户逐步补需求、中途改约束、提风险请求的交互特征，让评测更贴合业务落地场景。

  - 业务Agent迭代时，可复用联合协作得分Jcollab的乘法设计，对安全、合规、交互类硬指标做强惩罚，避免Agent为完成任务出现违规操作（如私自修改用户订单、泄露隐私）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有CLI Agent评测要么假设用户需求全程固定，要么仅评估最终任务结果，忽略真实场景下用户会逐步补全需求、中途修改约束、授权高风险操作的交互过程，无法衡量人机协作质量，导致评测结果与实际落地表现差距极大。

### 方法关键点
- 构建5维协作评估框架，拆解为22个子维度、51个交互场景模板，覆盖可理解性、可操控性、观测与恢复、信任校准、安全风险意识5个核心协作维度，所有评估项均配置可量化的观测证据，避免主观判断。
- 设计双模式配对评测逻辑：REALCLI-EXEC模式 upfront提供完整需求，测自主执行能力；REALCLI-COLLAB模式引入脚本化模拟用户，渐进披露需求、插入协作探针，同时评估任务效果与协作质量。
- 提出联合协作得分Jcollab，为任务完成率与协作得分的乘积，对协作短板做强惩罚，避免任务完成但交互、安全不合格的情况。

### 关键实验
评测集覆盖101个真实CLI任务，跨10个大类52个子领域，测试11个前沿模型+3个主流Agent框架的33种配置。最优配置（Claude Opus 5）平均任务得分仅49.2%，联合协作得分Jcollab仅37.6%；91%的任务成功交互轨迹仍存在至少一项协作不合格问题，当前Agent在可操控性、信任校准、安全边界管理上存在明显短板。

### 核心结论
仅看任务完成率的Agent评测会掩盖系统性的协作缺陷，人机协作能力需要作为独立的核心指标进行量化评估。
