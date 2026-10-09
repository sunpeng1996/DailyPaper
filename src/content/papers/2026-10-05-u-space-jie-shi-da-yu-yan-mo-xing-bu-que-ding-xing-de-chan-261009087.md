---
title: 'U-Space: Uncovering When and Why Uncertainty Arises in Language Models'
title_zh: U-Space：揭示大语言模型不确定性的产生时机与成因
authors:
- Tobias Braun
- Nils Loose
- Alexander Herzog
- Virginia Ceccatelli
- Marcus Rohrbach
- Thomas Eisenbarth
- Lorenzo Cavallaro
affiliations:
- Technische Universität Darmstadt
- University College London
- Universität zu Lübeck
- Mila – Quebec Artificial Intelligence Institute
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.09087'
url: https://arxiv.org/abs/2610.09087
pdf_url: https://arxiv.org/pdf/2610.09087
published: '2026-10-05'
collected: '2026-10-09'
category: LLM
direction: LLM 不确定性量化与可解释性
tags:
- Uncertainty Quantification
- Mechanistic Interpretability
- LLM
- Residual Stream
- Confidence Estimation
one_liner: 构建无需训练、可解释的LLM不确定性子空间，实现精准的不确定性归因与量化
practical_value: '- 电商导购/客服Agent可复用U-Space思路构建领域语义锚，零训练成本检测回答不确定性，减少虚假宣传、错误推荐类 hallucination
  带来的客诉

  - 生成式推荐场景下，可将U-LENS的token级不确定性归因能力结合RAG召回，当推理过程出现不确定性时自动触发补全检索，提升推荐理由的可信度

  - 评估LLM推理质量时，可借鉴长度控制的评估协议，避免把生成长度的相关性误判为不确定性估计的真实效果，提升离线评估的可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM越来越多地被用于高风险决策场景，但现有不确定性量化方法大多依赖多次生成或单独训练组件，输出的标量置信度无法揭示不确定性产生的位置和成因，且大量方法的预测效果高度依赖生成长度这一 shortcut，无法反映真实的不确定性捕捉能力。

### 方法关键点
- 定义歧义、信息不全、证据冲突、通用不确定性四类语义锚，通过J-LENS将锚点的词表方向映射回残差空间，相减得到各不确定性类别的对比方向，正交化后构建U-Space低维子空间
- 提出U-LENS读头，将每个token的隐状态投影到U-Space基向量上，得到token级的不确定性归因图；结合思考结束位置的二阶可解释不确定性信号与平均预测熵的一阶分布不确定性信号，相乘得到最终的推理级不确定性分数
- 全程无需标注、无需重复生成、无需额外训练，仅依赖预训练LLM的内部隐状态即可完成计算

### 关键实验
在Gemma 4、Qwen3.5、Magistral 1.1三个推理模型，MMLU-Pro、Omni-MATH、SuperGPQA、TriviaQA四个基准上测试，U-LENS平均AUROC达71.1%，比最强基线TokUR高1.5个百分点；长度控制后AUROC仅下降1.8个百分点，远低于TokUR的9.4个百分点，跨模型AUROC相对最优基线提升2.2~4.7个百分点。

**最值得记住的一句话**：LLM的不确定性不仅可通过隐空间语义方向量化归因，且可解释的二阶不确定性信号与一阶分布熵结合能获得远超现有基线的泛化性与抗长度干扰能力。
