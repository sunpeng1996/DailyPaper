---
title: Should I Be Polite to My LLM Relevance Judge? Tone as a Severity Operating-Point
  Shift
title_zh: 对LLM相关性判分器说话礼貌有用吗？语气可偏移其评估严格度工作点
authors:
- Tian Zhang
- Meng Li
affiliations:
- Independent Researcher
arxiv_id: '2609.09703'
url: https://arxiv.org/abs/2609.09703
pdf_url: https://arxiv.org/pdf/2609.09703
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: LLM-as-judge 评估稳定性研究
tags:
- LLM-as-judge
- relevance-assessment
- prompt-engineering
- evaluation
- prompt-tone
one_liner: 验证LLM相关性判分的语气影响来自严格度偏移而非能力变化，效果高度依赖模型
practical_value: '- 用LLM做离线相关性判分（如召回/排序效果评估、合成训练标签）时，固定prompt语气和措辞，避免绝对得分偏移，尤其用LLM输出做训练标签的场景需提前校准语气

  - 若仅用LLM做相对排序（如rerank粗筛），语气影响极小，最大NDCG@10波动仅0.011，无需过度纠结prompt礼貌程度

  - 对DeepSeek这类语气敏感的模型，可通过调整语气校准其判分严格度，对齐人工标注的严格水平，无需额外微调即可提升判分一致性

  - 做LLM judge评估时增加paraphrase对照，排除单个prompt措辞的偶发影响，区分全局语气效应和单个prompt异常波动'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM被广泛用作搜索推荐场景的相关性判分器，替代昂贵的人工标注产出训练标签或做离线效果评估，但LLM判分结果易受prompt表面特征干扰，过往关于prompt语气的研究结论相互矛盾，且未覆盖相关性判分场景，也无明确作用机制，从业者无法确定如何设置prompt语气保障判分稳定性。

### 方法关键点
1. 基于TREC DL19/DL20的3498条query-passage人工标注对，测试8个主流LLM判分模型；
2. 构造5个经polite-guard校准的礼貌等级（L1粗鲁到L5恭敬），每个等级配3个paraphrase，仅修改prompt wrapper，评分规则、输出格式完全一致，排除无关变量干扰；
3. 提出严格度工作点偏移机制，定义严格度偏差、语气漂移指标预测判分一致性变化方向，用query不相交的交叉拟合验证关联的鲁棒性。

### 关键结果
1. 语气敏感度高度依赖模型：仅DeepSeek V4 Flash有显著U型响应，粗鲁/恭敬语气相比中性可提升Cohen's κ约0.05，其余模型κ波动均小于0.015；
2. 交叉拟合验证对齐变化与一致性变化的Spearman ρ=-0.683，p=0.019，完全符合工作点偏移假设；
3. 语气对绝对校准指标的影响远大于排序：32组对比中NDCG@10最大波动仅0.011，排序一致性Kendall's τ最低为0.743。

**最值得记住的一句话**：调整LLM判分器的prompt语气本质是拧动其严格度旋钮，而非提升其判分能力，是否礼貌取决于当前模型严格度与人工参考标注的对齐程度。
