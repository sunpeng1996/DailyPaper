---
title: Claims of emergence in AI should be grounded in information decomposition
title_zh: AI领域的涌现主张应基于信息分解方法量化验证
authors:
- Christoph Riedl
- Fernando E. Rosas
affiliations:
- Northeastern University
- University of Sussex
arxiv_id: '2610.28479'
url: https://arxiv.org/abs/2610.28479
pdf_url: https://arxiv.org/pdf/2610.28479
published: '2026-10-20'
collected: '2026-10-22'
category: Other
direction: AI涌现量化 · 信息分解理论
tags:
- Partial Information Decomposition
- Emergence
- Multi-Agent System
- LLM Interpretability
- Human-AI Collaboration
one_liner: 提出基于部分信息分解的统一框架，跨尺度量化LLM、多Agent、人-AI协作的涌现与协同效应
practical_value: '- 多Agent系统优化：可通过PID量化Agent间的协同（synergy）与冗余（redundancy），用persona/ToM提示增加Agent差异化，平衡协同与冗余提升团队性能，可复用在电商多Agent客服、选品团队的架构设计

  - LLM微调/裁剪优化：LLM中间层是协同核心，RL微调时优先优化协同区域可获得更高性能增益；裁剪冗余层/头对简单任务影响极小，可用于推荐系统侧的LLM轻量化部署

  - 人-AI协作系统设计：可通过PID划分AI独有、人类独有、冗余、协同四类信息边界，针对性设计协同流程，比如电商运营人-AI选品场景，在高难度任务上最大化协同效应

  - 推荐系统多源信息融合：用PID区分用户行为、物品属性、上下文三类源的独特、冗余、协同信息，减少冗余特征的计算开销，重点挖掘跨源协同信息提升推荐精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前AI领域对“涌现”“协同”的定义缺乏统一可量化的标准，不同领域（LLM可解释性、多Agent系统、人-AI协作）的相关主张无法横向对比、甚至无法证伪，阻碍了跨领域的研究进展与工程落地。

### 方法关键点
- 采用部分信息分解（PID）作为统一框架，将多源变量对目标的互信息拆分为3类核心信息原子：单源独有的独特信息、多源共享的冗余信息、仅多源联合才能提取的协同信息
- 针对高维场景下全量分解计算量爆炸的问题，给出4种实用优化策略：仅计算目标原子、用低阶分解近似、小批量子集分解聚合、用O-information等标量摘要量化协同-冗余净平衡
- 提出3种可落地的涌现量化测试：涌现容量测试（两两源的协同信息是否大于0）、独特信息准则（宏观特征是否包含微观组件没有的预测信息）、实用准则（宏观自预测能力是否超过所有微观组件的总和）

### 关键结果数字
- LLM实验：在Llama 3、Qwen 3、DeepSeek V2 Lite等模型上验证，中间层为协同核心，裁剪协同头对复杂任务的性能损伤是裁剪冗余头的3倍以上；RL微调协同区域的性能增益比微调冗余区域高40%以上
- 多Agent实验：添加ToM提示的Agent组的协同得分比无提示组高28%，总稳定性提升超过10倍（p=2.9×10^-14）
- 人-AI协作实验：在AI无法单独解决的高难度任务上，人-AI协同的正确率比人类单独作业高80%，其中协同信息贡献占比超过70%

最值得记住的一句话：任何复杂系统的性能收益都来自冗余（鲁棒性）与协同（效率）的平衡，没有差异化组件的系统无法产生真正的协同与涌现。
