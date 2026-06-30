---
title: 'TACO: Tool-Augmented Credit Optimization for Agentic Tool Use'
title_zh: TACO：面向智能体工具调用的工具增强信用分配优化
authors:
- Mingkuan Feng
- Jinyang Wu
- Hao Gu
- Fangrui Lv
- Ruihan Jin
- Chuyuan Zhang
- Zhengqi Wen
- Jianhua Tao
affiliations:
- Tsinghua University
- Chinese Academy of Sciences
arxiv_id: '2606.30251'
url: https://arxiv.org/abs/2606.30251
pdf_url: https://arxiv.org/pdf/2606.30251
published: '2026-06-28'
collected: '2026-06-30'
category: Agent
direction: Agent工具调用 · RL信用分配
tags:
- Reinforcement Learning
- Credit Assignment
- Tool Use
- GRPO
- Agentic AI
one_liner: 针对代码工具智能体提出GRPO变体TACO，实现无外部评判器的工具调用信用分配
practical_value: '- 多工具调用Agent训练可借鉴差分探测归因思路：通过工具调用前后的结果差分计算单个调用的价值，不需要额外外部 judge 模型，大幅降低训练成本

  - 可复用OGAR的结果门控路由规则：只给对最终结果负责的token分段分配奖励，既避免惩罚正确的前置推理，也自动抑制无效冗余调用，不需要额外加工具调用惩罚项

  - 对抗奖励作弊可借鉴差分思路：差分抵消了公共偏移，天然对提前泄露答案的作弊行为鲁棒，不需要额外设计正则机制

  - 落地Agent可追求准确率与推理效率双赢：通过训练引导Agent仅在必要时调用工具，可同时提升准确率和降低端到端延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码工具智能体训练仅给整条轨迹分配最终答案奖励，无法区分单个工具调用是有用、冗余还是误导；现有过程奖励要么无法给单个调用归因，要么依赖外部 judge 模型增加成本，还存在probe hacking奖励作弊问题，最终导致模型过度调用工具，既降低准确率又升高推理延迟，亟需低成本准确的工具调用信用分配方法。
### 方法关键点
- 提出GRPO的变体TACO，设计耦合的双优势通道做训练；
- 差分答案探测奖励（DAPR）：在工具调用前后插入轻量探测，分别输出无工具/有工具条件下的模型答案，用两者结果正确性的差值作为该工具调用的奖励；差分抵消了模型预工具阶段已有的知识，天然抗probe hacking，复用现有答案校验器，不需要额外外部模型；
- 结果门控优势路由（OGAR）：无参数规则，根据工具调用结果将最终答案的优势仅路由给负责该结果的token分段，分四种场景合理分配奖惩，不需要额外工具调用惩罚项；
- 训练采用两阶段SFT+RL pipeline。
### 关键结果
在12个多模态基准（感知、推理、通用三类）测试：7B规模的TACO平均准确率达68.1%，比此前最佳开源代码工具Agent高4.4个百分点，比GPT-4o高9.6个百分点；同时是推理延迟最低的模型，验证了减少无效调用可同时提升效果和效率；ablation显示DAPR贡献4.5个点收益，OGAR贡献2.0个点，方法不绑定backbone，给Qwen3-VL-8B也能带来5.9个点提升。
### 核心结论
只有给单个工具调用分配匹配其实际贡献的信用，才能让Agent学会合理调用工具，同时获得准确率和效率的双赢
