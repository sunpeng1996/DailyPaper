---
title: Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity
  Familiarity from Factual Reliability Across Model Scale
title_zh: Bielik模型认知边界检测：激活离散度跨规模区分实体熟悉度与事实可靠性
authors:
- Grzegorz Brzezinka
affiliations:
- Prosit AS
arxiv_id: '2607.07670'
url: https://arxiv.org/abs/2607.07670
pdf_url: https://arxiv.org/pdf/2607.07670
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM幻觉检测 · 内部激活表征探测
tags:
- Hallucination Detection
- Activation Probing
- LLM Interpretability
- Unsupervised Detection
- Factual Reliability
one_liner: 基于MLP后SwiGLU激活离散度的无监督单前向传播方法，检测LLM实体熟悉度AUROC最高达1.00
practical_value: '- 做Agent工具调用前置判断时，可以用单前向传播的IPR/谱熵指标快速识别用户query中涉及的实体是否在LLM知识库覆盖范围内，避免无意义调用或幻觉输出，比多采样语义熵成本低80%

  - 垂直领域LLM微调时，可以用激活离散度作为评估指标，快速判断新增实体的知识注入是否成功，无需额外标注

  - 电商生成式商品/内容推荐场景中，可加入该轻量检测模块过滤LLM生成的不存在的商品、品牌等虚构实体，降低badcase率

  - 注意：该指标仅能检测实体熟悉度，无法区分已知实体下的回答是否正确，事实类校验仍需搭配语义熵等多采样方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM幻觉检测方案要么依赖多采样+辅助模型推理成本高，要么需要监督标注泛化性差，且未明确区分「实体是否被模型见过」和「已知实体的回答是否正确」两个独立维度，小语种模型的相关内部表征探测研究也存在空白。
### 方法关键点
- 测试4个不同参数规模（1.5B~11B）的波兰Bielik指令微调模型，覆盖运动员、城市、作家、音乐家4类实体域，每类包含42个知名、42个小众真实、42个形态合理的虚构实体，共504条prompt/模型
- 提取prompt最后token位置的SwiGLU后MLP激活，计算无监督指标逆参与率（IPR）和谱熵，对比监督线性探针、token长度基线、5采样语义熵基线
- 设计跨域迁移、prompt模板控制、实体真实性对照实验排除lexical混淆变量
### 关键结果
- 无监督离散度指标区分知名vs虚构实体AUROC达0.95~1.00，监督线性探针达0.99~1.00，远超0.70~0.74的选择感知置换基线，跨实体域迁移平均AUROC达0.92~0.99
- 实体熟悉度检测效果在1.5B小模型上已达天花板，而事实回答准确率随规模提升明显：严格判据下1.5B/4.5B/7B/11B对知名运动员的全对回答占比分别为0%/4.8%/23.8%/45.2%
- 5采样语义熵在熟悉度检测上AUROC仅0.71~0.83，但在已知实体下的幻觉检测上AUROC最高达0.87，和离散度指标能力完全互补
> 最值得记住：激活离散度检测的是LLM有没有见过某个实体，而不是它能不能正确回答该实体的相关问题，二者是完全独立的优化维度
