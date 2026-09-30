---
title: 'VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video
  Agents'
title_zh: VideoLoop：双循环工作记忆缓解长视频Agent语义抖动
authors:
- Jinfa Huang
- Jianming Xu
- Jingyang Lin
- Zhengyuan Yang
- Jiebo Luo
affiliations:
- University of Rochester
- Microsoft
arxiv_id: '2609.38119'
url: https://arxiv.org/abs/2609.38119
pdf_url: https://arxiv.org/pdf/2609.38119
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: 长视频多模态Agent · 工作记忆优化
tags:
- Multimodal-Agent
- Working-Memory
- Long-Video-Understanding
- Semantic-Thrashing
- Dual-Loop-Architecture
one_liner: 提出双循环架构长视频Agent，通过可重写 bounded 工作记忆解决语义抖动问题
practical_value: '- 长会话/长视频推荐Agent可复用双循环记忆架构：外循环负责用户交互/内容探索，内循环定时重写 bounded 工作记忆，避免
  append-only 带来的上下文噪声稀释关键信息，适配有限 LLM context 窗口

  - 可复用三级存储设计：Tier1 是当前推理用的小容量高优先级工作记忆，Tier2 是压缩的历史行为/交互清单，Tier3 是无损存储的全量交互/内容物料，兼顾检索效率和信息不丢失，适合长周期用户建模、直播内容理解等场景

  - 语义抖动的量化方式可直接借鉴：用「当前上下文单独回答问题的准确率」作为记忆质量的评估指标，不用依赖模型全链路推理结果，能快速定位记忆模块的性能瓶颈'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长视频理解需要多模态Agent多步迭代收集分散证据，但现有 append-only 工作记忆随着迭代不断累积噪声，关键证据的注意力被稀释，出现 semantic thrashing 问题：Agent推理开销不断上升但效果反而下降，类似操作系统的内存抖动。理论推导证明 append-only 记忆只能新增证据无法删除冗余，是结构性缺陷而非调优问题。

### 方法关键点
- 双循环架构：外循环为多模态推理Agent，负责视频探索、工具调用，所有观测和中间结果都写入无损的无限容量沙箱文件系统；内循环为记忆编排器，每次外循环执行后从文件系统检索和query相关的证据，重写固定大小的 bounded 工作记忆
- 三级存储分层：Tier1 是对外暴露的32K token bounded工作记忆，分元数据、证据、待查目标等6个结构化区块；Tier2 是压缩的历史行为清单，只保留关键动作参数；Tier3 是无损存储的全量帧、脚本、分析结果
- 记忆重写规则：编排器每次对工作记忆执行UPDATE/APPEND/DELETE操作，保证工作记忆始终不超过token预算，同时最小化与目标证据集的对称差

### 关键实验
在VideoMME(long)、VideoMMMU、LongVideoBench(long)三个长视频基准测试，可适配4种主流LVLM backbone，平均提升4.2%准确率；用Gemini 3.1 Pro时三个基准分别达到88.3%、88.8%、80.9%，比原生LVLM最高提升5.1个百分点；最难的25%问题上，仅读取工作记忆的盲测准确率达81.1%，比append-only基线高20.2个百分点，token开销仅比基线高0.5%。

最值得记住的一句话：长 horizon Agent的记忆应该被主动 curated，而不是被动 accumulated。
