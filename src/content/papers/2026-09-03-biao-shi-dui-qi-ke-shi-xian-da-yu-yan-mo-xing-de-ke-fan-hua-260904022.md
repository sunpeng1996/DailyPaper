---
title: Representational alignment yields generalizable safety in language models
title_zh: 表示对齐可实现大语言模型的可泛化安全性
authors:
- Lingyu Li
- Yan Teng
- Yingchun Wang
- Xia Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.04022'
url: https://arxiv.org/abs/2609.04022
pdf_url: https://arxiv.org/pdf/2609.04022
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM安全对齐 · 隐表示结构优化
tags:
- LLM Alignment
- Representational Learning
- Adversarial Robustness
- Safety
- Prototype Learning
one_liner: 提出表示相似度优化ReSO方法，对齐LLM内部隐表示与人类道德分类，大幅提升对抗场景安全鲁棒性
practical_value: '- 做Agent安全对齐时可复用ReSO思路：无需仅监督输出，直接对齐业务规则/禁止行为的隐表示结构，能大幅提升对抗prompt绕过的防御能力，比如避免电商客服被诱导输出违规话术

  - 现有DPO等偏好对齐方法会降低对抗鲁棒性的结论可直接复用：业务做LLM对齐时需同时监控标准测试集指标和对抗攻击成功率，避免表面合规但易被绕过

  - 可复用原型表示+相似度排序优化的训练范式：对搜索推荐的用户/物品语义表示对齐，比如对齐用户行为隐表示与业务价值分类（如高价值/低价值/风险行为），提升跨场景推荐的规则一致性

  - 隐表示RSA（表示相似度分析）指标可复用为对齐效果的前置评估指标：不用等全量端到端测试，直接计算隐表示与目标结构的相关性即可预判泛化效果，降低迭代成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前主流LLM对齐方法（DPO、RLHF等）仅优化输出层面的合规性，在面对重述、伪装等形式的对抗jailbreak攻击时极易被绕过，而人类可基于原型化的道德分类体系，跨语言形式识别同一有害意图。经测试23款不同规模、不同对齐阶段的开源LLM，均存在内部道德概念分类结构模糊、典型度梯度弱的问题，是安全泛化性差的核心原因。
### 方法关键点
- 基于Social-Chemistry-101数据集构建251334条带置信度加权典型度的人类道德判断参考，将每个行为映射为10维稀疏向量（对应MFT道德框架的5对善恶维度）
- 提出ReSO（Representational Similarity Optimization）训练范式：直接优化LLM各层隐表示的相似度关系，使其与人类道德分类的相似度结构对齐，无需监督生成的响应文本
- 训练目标由两部分组成：结构损失用Bradley-Terry排序目标约束隐表示相似度与人类判断的排序一致性，保留损失用KL散度约束模型通用能力不下降
### 关键结果
- 对比同训练数据下的DPO基线，ReSO在全系列模型上一致降低对抗攻击成功率：Qwen3-8B的HarmBench ASR从26.17%降至14.72%，已做强安全对齐的gpt-oss-20B的HarmBench ASR从3.33%进一步降至1.33%
- DPO虽提升标准道德判断准确率，但会使所有模型的对抗攻击成功率上升，Qwen3-8B的HarmBench ASR升高11.41个百分点
- 隐表示相似度指标RSA与对抗攻击成功率ASR的拟合R²达0.86，可直接预判安全泛化效果

**最值得记住的结论**：仅优化输出层面的对齐只能获得表面合规性，对齐内部隐表示的概念结构才能实现跨场景、对抗条件下的可泛化安全。
