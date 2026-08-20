---
title: Temporal Multi-Signal Fusion for Token-Level Hallucination Detection
title_zh: 面向Token级幻觉检测的时序多信号融合方法
authors:
- Igor Itkin
affiliations:
- Independent Researcher
arxiv_id: '2608.18115'
url: https://arxiv.org/abs/2608.18115
pdf_url: https://arxiv.org/pdf/2608.18115
published: '2026-06-29'
collected: '2026-08-20'
category: LLM
direction: 大模型幻觉检测 · 黑盒时序融合
tags:
- Hallucination Detection
- Temporal Modeling
- Multi-Signal Fusion
- RAG
- Sequence Labeling
one_liner: 黑盒场景下通过时序多信号融合+序列标注实现Token级幻觉检测，较单Token基线AUC提升11点
practical_value: '- 做RAG业务的幻觉检测时，可直接复用33维多信号特征体系（文本统计+NLI+LM surprisal+时序衍生特征），无需访问生成模型内部，适配闭源API场景

  - 幻觉通常是连续Span（中位数5个Token，持续概率90.2%），放弃单Token独立判断，用BiGRU/1D-CNN做序列标注能显著提升检测效果，仅需121K参数即可达到SOTA水平

  - 训练幻觉检测模型时，优先选择高标注密度的数据集（正样本占比高），比大样本量但稀疏标注的数据集泛化性更好

  - 若有开源模型白盒访问权限，可将该方法的黑盒特征与Attention类特征融合，能再提升2~3个点AUC'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Token级幻觉检测均采用单Token独立打分范式，在LLM高置信度错判的场景完全失效，且大多需要访问模型内部，无法适配闭源API场景；而幻觉本质是连续的时序Span，相邻Token的信号存在强相关性，现有方法完全浪费了该时序信息。

### 方法关键点
- 特征层：融合三类外部信号生成33维per-Token特征，包括20维文本统计特征（上下文重叠、时序衍生的均值/差分/窗口极值等）、7维NLI特征（DeBERTa输出的蕴含/矛盾概率及时序衍生特征）、6维LM特征（TinyLlama输出的surprisal、熵等），全程无需访问生成模型内部
- 建模层：将幻觉检测转为序列标注任务，用2层BiGRU（隐层64，仅121K参数）做序列建模，训练采用类别平衡的BCE损失
- 校准优化：CRF模型的softmax打分存在严重校准偏差，采用前后向边缘概率计算最多可提升17.9个AUC点

### 关键结果
- 在RAGTruth数据集10种子实验中，BiGRU达到0.840 AUC，比单Token LogReg基线高11个点（p=0.002）
- 跨模型泛化：在6种未见过的生成LLM上测试，AUC仅下降不足4%
- 分解实验显示：时序结构贡献44%的性能增益，多信号融合贡献24%，模型容量仅贡献32%；不同序列架构（BiGRU/Mamba/Transformer）性能天花板一致（0.843~0.845 AUC），瓶颈在特征集而非模型结构

### 核心结论
幻觉不是单点事件，而是连续的时序Span，76%的标签熵仅通过前一个Token的标签即可消除，单Token独立判断的设计天然存在性能天花板。
