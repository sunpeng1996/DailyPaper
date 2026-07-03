---
title: 'DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language
  Models'
title_zh: 《DRIFTLENS：个性化大模型记忆诱导推理漂移度量框架》
authors:
- Xi Fang
- Weijie Xu
- Yingqiang Ge
- Yuhui Xu
- Stephanie Eckman
- Chandan K. Reddy
affiliations:
- Amazon
arxiv_id: '2607.02374'
url: https://arxiv.org/abs/2607.02374
pdf_url: https://arxiv.org/pdf/2607.02374
published: '2026-07-02'
collected: '2026-07-03'
category: Eval
direction: LLM个性化 · 推理稳定性评估
tags:
- Personalized-LLM
- Reasoning-Drift
- Evaluation-Framework
- DPO
- GRPO
- Memory-Augmented
one_liner: 提出无真值推理漂移度量框架DRIFTLENS，验证记忆引发漂移并评估DPO/GRPO的缓解效果
practical_value: '- 搭建带用户记忆的电商导购/咨询Agent时，可复用DRIFTLENS的无真值推理稳定性评估流程，检测无关用户属性（如年龄/职业）是否干扰商品推荐、纠纷调解等场景的推理逻辑，降低隐性偏见风险

  - 优化个性化LLM稳定性时，可复用论文后训练trick：DPO搭配强模型风格归一化的偏好对，或GRPO引入格式奖励+DTW/SRI漂移奖励，在几乎不损失通用能力的前提下降低推理漂移

  - 构建无标准答案类任务（如消费决策建议、售后问题处理）的评估体系时，可复用「无记忆回答为基线+推理步骤符号化映射+序列相似度度量」的范式，替代高成本人工标注'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前个性化LLM普遍通过注入用户记忆实现定制化交互，但在无客观标准答案的开放决策类任务（如消费建议、职场咨询）中，无关用户属性记忆会悄悄改变模型推理路径，仅看最终回答无法察觉这种漂移，现有准确率指标完全无法检测，易导致推荐/建议出现隐性偏见。

### 方法关键点
- 框架4核心组件：① 经LLM+人工两轮过滤的422条persona无关、需权衡推理、无真值的开放问题数据集；② 78轮迭代优化的4大类11小类价值本体，将自由文本推理步骤映射为离散符号，跨模型标注一致性达83%；③ 三类受控扰动（负控制：无意义噪声；正控制：重大人生事件；实验组：用户属性记忆）；④ 两个互补漂移度量：DTW捕捉推理步骤顺序变化，SRI同时捕捉顺序和符号分布变化。
- 缓解策略：对比GRPO（将DTW加入奖励函数）和DPO（用扰动鲁棒偏好对训练）两种后训练方案。

### 关键实验
在4款主流LLM、10类用户属性上测试：① 无关用户属性记忆引发的漂移显著高于噪声基线，Cohen's d达0.35~0.98，跨性别、年龄、职业、残疾等维度均存在；② GRPO/DPO均能有效降低漂移，最多可将DTW降低40%（Gemma2-2B从0.309降至0.186），多数场景下不损失MMLU/GSM8K等通用能力，还可提升回答有用性。

### 核心结论
部署带记忆的个性化LLM用于决策类场景前，必须先评估推理稳定性，否则看似合理的回答可能隐藏受无关属性干扰的偏差。
