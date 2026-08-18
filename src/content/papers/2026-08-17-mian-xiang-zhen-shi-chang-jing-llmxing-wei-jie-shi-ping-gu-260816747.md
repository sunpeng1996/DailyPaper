---
title: Would this change your answer? Evaluating Explanations of LLM Behavior In The
  Wild with Counterfactual Experiments
title_zh: 面向真实场景LLM行为解释评估的反事实实验框架CHIVE
authors:
- Adam Karvonen
- Euan Ong
- Subhash Kantamneni
- Samuel Marks
affiliations:
- Anthropic
- Anthropic Fellows Program
arxiv_id: '2608.16747'
url: https://arxiv.org/abs/2608.16747
pdf_url: https://arxiv.org/pdf/2608.16747
published: '2026-08-17'
collected: '2026-08-18'
category: Eval
direction: LLM可解释性评估 · 反事实实验
tags:
- Interpretability
- Counterfactual
- Agent Pipeline
- LLM Evaluation
- Self-Explanation
one_liner: 提出自动挖掘真实场景LLM异常行为、通过反事实实验验证解释的Agent管道，更新可解释性工具评估结论
practical_value: '- 做LLM Agent/生成式推荐bad case归因时，可直接复用CHIVE四步pipeline：采样多轮响应→筛异常行为→做反事实prompt编辑验证→归因，定位prompt影响因素的准确性远高于人工拍脑袋。

  - 现有基于激活的可解释性工具（SAE、激活oracle等）对真实场景自然行为归因无增益，业务侧无需浪费资源接入这类工具，直接做反事实prompt测试性价比更高。

  - 若要训练LLM自我归因能力，可采用CHIVE生成的反事实标注数据训练，泛化性优于人工构造的hint场景数据，能覆盖真实业务中的多样异常行为。

  - 可复用论文的反事实claim标注范式，标注业务场景的prompt敏感性数据，优化生成式推荐/客服Agent的prompt鲁棒性。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM可解释性、思维链忠实度领域的解释方法缺乏统一有效的评估标准，过往评估依赖人工植入提示特征的狭窄实验场景，无法反映真实业务中自然发生的LLM异常行为的归因需求，亟需能规模化生成带反事实验证标注的真实行为数据集的方案。

### 方法关键点
- 提出CHIVE Agent pipeline，四步自动生成归因数据：① 目标LLM在大规模真实prompt（WildChat为主）上采样30次响应；② 大模型筛查出低概率异常行为；③ 自动生成5-15组反事实prompt编辑实验，统计行为发生率变化；④ 独立大模型验证解释的有效性。
- 单条归因数据包含两类标注：开放域行为原因解释，以及二分类反事实claim标签（判断特定prompt编辑是否会改变当前行为）。
- 落地两类场景：一是作为基准评估现有可解释性工具的实际增益，二是用生成的标注数据训练LLM的自我行为预测能力。

### 关键结果
- 评估三类主流激活类可解释性工具（激活oracle、自然语言自编码器NLA、稀疏自编码器SAE），所有工具均未给反事实预测任务带来任何精度提升，跨2个目标模型、3个预测模型家族结果一致。
- 用CHIVE生成的数据训练LLM预测自身行为变化，在分布外PETRI数据集、人工hint场景数据集上AUROC相对基线提升10~15pp，性能接近Claude Opus水平，且无证据表明模型归因存在内部状态特权访问。

最值得记住的结论：对于真实场景下的LLM行为归因，直接做低成本的反事实prompt编辑实验，性价比远高于接入复杂的激活类可解释性工具。
