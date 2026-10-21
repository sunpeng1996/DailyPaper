---
title: Measuring Mechanistic Uncertainty in Large Language Models via Causal Robustness
title_zh: 基于因果鲁棒性的大语言模型机制性不确定性度量方法
authors:
- Aneesh Komanduri
- Majid Afshar
- Timothy A. Miller
- Yanjun Gao
affiliations:
- University of Colorado Anschutz Medical Campus
- University of Wisconsin-Madison
- Harvard Medical School
- Boston Children's Hospital
arxiv_id: '2610.22636'
url: https://arxiv.org/abs/2610.22636
pdf_url: https://arxiv.org/pdf/2610.22636
published: '2026-10-14'
collected: '2026-10-21'
category: LLM
direction: 大语言模型 · 不确定性量化
tags:
- Uncertainty_Quantification
- Causal_Robustness
- Mechanistic_Interpretability
- Jlens
- LLM_Reliability
one_liner: 提出基于LLM内部干预敏感性的因果鲁棒性裕度指标，可补充传统输出端不确定性量化方法
practical_value: '- 高可靠性Agent场景（电商客服、合规导购、推荐理由生成）可将因果鲁棒性裕度作为新增置信度特征，与传统输出端熵、自洽性特征融合，错误回答识别AUROC最高可提升9.9个百分点。

  - 领域知识注入SFT（如电商商品/活动知识、垂类规则注入）场景，可将因果鲁棒性裕度作为无监督评估指标，裕度提升明显说明知识点掌握更稳定，无需大量标注即可校验SFT效果。

  - 私有化部署白盒LLM场景可复用Jlens干预方法做错误回答修复，实验显示最高可恢复52.2%的错误回答，无需重新生成即可提升问答准确率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM不确定性量化（UQ）方法多基于输出端信号（token熵、自洽性、语义熵等），无法反映模型内部计算的稳定性，在高风险场景（医疗、电商合规问答）下难以解释不确定性来源，且对错误回答的识别精度存在瓶颈，亟需可解释的、基于内部机制的不确定性信号。

### 方法关键点
- 定义机制性不确定性为支撑模型输出的内部计算的因果脆弱性，用因果鲁棒性裕度α*量化：使输出发生语义偏移所需的最小内部干预强度，值越小不确定性越高。
- 基于Jlens（Jacobian Lens）实现干预：抽取模型中后10层的共识token向量，沿该向量对中间层激活做层归一化的加减干预，搜索触发输出语义变化的最小α值。
- 指标无需标注监督，完全通过干预敏感性计算得到。

### 关键实验
在TriviaQA、PopQA、MedQA等5个问答数据集、Llama-3.1-8B、Qwen2.5-7B、Gemma-3-12B共3个开源LLM上测试：
1. 用-α*识别错误回答的AUROC最高达0.75，正确回答的平均α*是错误回答的1.5~3.2倍。
2. 将α*与传统输出端UQ特征融合，错误识别AUROC最多可提升9.9个百分点，尤其在传统方法表现差的TruthfulQA数据集上增益明显。
3. 知识注入SFT后，新答对的问题α*平均提升0.032，说明知识掌握更稳定。

### 最值得记住的一句话
LLM回答的可信度不仅和输出分布的一致性相关，更和支撑输出的内部计算的干预鲁棒性正相关，内部越稳定的回答正确率越高。
