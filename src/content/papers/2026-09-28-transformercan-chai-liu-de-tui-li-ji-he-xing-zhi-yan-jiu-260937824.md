---
title: The Geometry of Inference in Transformer Residual Streams
title_zh: Transformer残差流的推理几何性质研究
authors:
- Timur Mudarisov
- Mikhail Burtsev
- Radu State
affiliations:
- University of Luxembourg
- London Institute for Mathematical Sciences
arxiv_id: '2609.37824'
url: https://arxiv.org/abs/2609.37824
pdf_url: https://arxiv.org/pdf/2609.37824
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: LLM内部表示 · 残差流几何分析
tags:
- Transformer
- Residual Stream
- Representation Geometry
- LLM Interpretability
- Inference Mechanism
one_liner: 揭示Transformer残差流推理过程的几何收敛规律，验证几何推理假说
practical_value: '- 做LLM4Rec早退出推理优化时，优先用余弦相似度而非欧氏距离判断中间层表示收敛性，余弦竞争收敛更早，可提前终止推理降低时延与计算成本

  - 做生成式推荐候选排序时，可复用文中「竞争集」思路，用最终端点距离关联token/候选项排序，提升相关性校准精度

  - 做LLM推理加速时，可参考文中几何特性优化KV cache裁剪策略，对收敛到低竞争集的层裁剪冗余表示，降低显存占用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有研究仅证实Transformer中间层存在最终预测的相关信息，但残差更新如何逐步区分最终目标表示与其他可能表示的过程尚不明确，缺乏几何层面的定量解释。

### 方法关键点
- 提出几何推理假说，定义「竞争集」：将其他上下文的最终残差状态作为端点库，与中间层状态的距离小于自身最终端点的端点构成竞争集，竞争集越小表示几何特异性越高
- 设计欧氏距离、余弦距离两类度量，结合Jaccard重叠率、竞争占比等指标追踪竞争集随模型深度的演化规律
- 构建高维理论模型分离范数、对齐度、端点几何的作用，证明直线收敛路径下竞争集必然严格嵌套

### 关键实验
在Gemma、Qwen2.5、Mistral、Llama3共6款主流预训练LLM上测试，使用FineWeb数据集的1024条256token上下文，对比均匀球、单vMF、vMF混合、投影正态等5种端点分布模型。核心结果：1）所有模型最早层就已出现对自身端点的平均偏好，但仍存在数百个竞争端点，余弦竞争集收敛远早于欧氏距离；2）余弦竞争集存在新增成员，说明实际收敛路径并非直线；3）投影正态模型预测竞争集准确率最高，比均匀球基线误差低4.6~7.5倍。

### 核心结论
Transformer残差流的推理收敛是定向对齐而非单纯距离缩短的过程，余弦距离比欧氏距离更能反映中间表示的特异性
