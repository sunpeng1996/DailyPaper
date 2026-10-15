---
title: Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive
  Feedback
title_zh: 基于弱交互反馈的任务对齐相似度贝叶斯测试时推理方法
authors:
- Weida Liang
- Kenji Kawaguchi
affiliations:
- National University of Singapore
arxiv_id: '2610.18656'
url: https://arxiv.org/abs/2610.18656
pdf_url: https://arxiv.org/pdf/2610.18656
published: '2026-10-13'
collected: '2026-10-15'
category: Reasoning
direction: 测试时推理 · 自适应相似度选择
tags:
- Bayesian_Inference
- Test_Time_Adaptation
- Similarity_Matching
- Feedback_Driven
- Retrieval
one_liner: 提出免训练BASIS框架，通过弱交互反馈自适应选择相似度准则，提升多场景候选选择性能
practical_value: '- 电商多模态召回/个性化排序场景可复用自适应权重方案：提前预计算语义、实体、价格、风格、实用性等多维度相似度分，测试时通过用户点击、收藏、pairwise偏好等弱反馈实时更新各维度权重，解决固定权重无法适配不同用户偏好的问题，尤其适合服饰、家居等用户审美差异大的品类

  - 电商导购Agent/RAG问答系统可复用探针选择逻辑：通过最大化预期信息增益选择下一轮交互问题，用最少的交互轮次定位用户真实需求，降低多轮澄清的用户流失率

  - 线上部署可直接复用其 fallback 设计：当判定当前准则库无匹配维度时自动回退到预调固定权重基线，避免效果骤降，降低上线风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM系统在检索样本、排序候选、优化响应时依赖固定相似度准则，不同任务、实例的最优对齐准则差异极大：数学推理选样看重推理结构匹配，文案精修看重风格一致性，固定权重或单一准则易出现对齐偏差，现有反馈驱动方法仅能优化候选排序，无法推断当前场景的最优匹配准则。
### 方法关键点
- 免训练BASIS框架，提前定义包含语义、词汇、实体、结构、风格等维度的任务专属相似度准则库
- 维护候选目标与匹配准则的联合后验分布，支持标量打分、pairwise偏好、验证器输出三类弱反馈的贝叶斯更新
- 按预期信息增益选择下一轮交互探针，最小化定位最优准则与候选的交互轮次
- 最终通过准则后验加权的动态效用函数排序候选，无需微调任何预训练模型
### 关键实验
在概念恢复、GSM8K/BBH推理示例选择、Anthropic HH/OpenAssistant响应精修三类任务测试，对比预调静态混合、同算力best-of-N等基线：6探针概念恢复Success@1从56.0%提升至68.1%，推理准确率从72.3%提升至73.1%，响应精修胜率从61.4%提升至63.8%；准则错配、候选池更大的场景增益更高，推理任务256候选池下相对静态混合提升2.8个百分点。
### 核心结论
固定权重的多准则融合无法适配实例级的准则偏移，仅靠弱交互反馈实现的自适应准则加权，可在几乎无额外训练成本的前提下稳定提升多场景候选选择效果
