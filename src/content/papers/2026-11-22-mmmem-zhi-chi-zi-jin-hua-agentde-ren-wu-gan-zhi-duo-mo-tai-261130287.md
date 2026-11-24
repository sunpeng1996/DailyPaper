---
title: 'MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation'
title_zh: MMMem：支持自进化Agent的任务感知多模态经验整合框架
authors:
- Yuxuan Chen
- Changwei Lv
- Yunfei Li
- Zhongjing Du
- Kehui Tan
- Zijun Liao
- Ruochong Zheng
- Hao Chen
- Can Deng
- Zheni Zeng
affiliations:
- Peking University
- Clemson University
- Nanjing University
- Tsinghua University
arxiv_id: '2611.30287'
url: https://arxiv.org/abs/2611.30287
pdf_url: https://arxiv.org/pdf/2611.30287
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: 多模态Agent · 长时记忆自进化
tags:
- Multimodal Agent
- Long-term Memory
- Experience Consolidation
- Self-improving
- LoRA
one_liner: 提出任务感知多模态记忆框架，结合外部经验整合与参数微调实现Agent自进化
practical_value: '- 多模态记忆构建可借鉴源链接多视图设计：对电商/广告场景的用户会话、商品图片、浏览记录按实体/时间维度分组，补充跨记录融合的场景表征用于检索，提升多模态内容匹配准确率

  - 冷启动与模型优化可复用任务生成+双目标训练策略：从历史业务数据生成QA对，用LoRA同时微调模型的证据回答与经验蒸馏能力，上线前用暖生成的经验预填充记忆库，降低冷启动误差

  - 经验管理可复用分级留存机制：新产生的推荐/问答经验先进入 staging 区，经过至少2次业务验证被复用后再永久留存，无访问自动过期，平衡记忆效用与存储成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent记忆仅存储原始交互记录，未固化任务执行中得到的跨模态关联结论，同类任务重复执行时会反复重建证据关联、重复犯错；同时现有方法很少同时优化外部记忆组织与模型参数适配，长时多模态交互下推理准确率低。

### 方法关键点
- 源链接多视图记忆：每个记忆节点存储原始文本、图片、OCR页面、跨记录融合生成的场景图四类视图，所有内容保留源ID可溯源
- 双层级自进化策略：一是记忆暖启动，从原始数据生成QA对预生成经验填充记忆库，参数固定；二是LoRA自训练，用跨域生成的QA对同时训练模型的证据回答与经验蒸馏两个目标，backbone固定
- 任务感知经验管理：执行任务时同时召回原始证据与历史经验，完成任务后自动蒸馏结构化经验（含任务上下文、结论、源链接），经验分级留存，需经过至少2次源验证的复用才会永久存储，无访问自动过期

### 关键结果
在3个多模态记忆基准（LoCoMo、Mem-Gallery、LooGLE v2）上对比8个基线（Mem0、A-Mem、Dense RAG等），使用Qwen3.5-9B时相对最优基线分别获得36.9%、17.6%、15.2%的提升，其中自训练与暖启动贡献了主要收益，生成视图与经验召回分别带来1-6个点的准确率提升。

**最值得记住的一句话**：Agent记忆的核心价值不是存储原始记录，而是固化任务执行过程中得到的、有来源支撑的可复用结论，同时对齐外部记忆组织与模型参数的任务适配能力才能最大化记忆效用。
