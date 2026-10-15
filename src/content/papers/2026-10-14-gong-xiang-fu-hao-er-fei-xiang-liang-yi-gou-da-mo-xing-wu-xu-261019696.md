---
title: 'Share the Symbol, Not the Vector: Training-Free Fact Communication Across
  Language Models'
title_zh: 共享符号而非向量：异构大模型无需训练的事实通信机制
authors:
- Xin Li
- Mengbing Liu
- Hao Jiang
- Xin Gao
- Annan Wang
- Xingwei Qu
- Yichi Zhang
- Chau Yuen
affiliations:
- Nanyang Technological University
- Yale University
- University of Manchester
arxiv_id: '2610.19696'
url: https://arxiv.org/abs/2610.19696
pdf_url: https://arxiv.org/pdf/2610.19696
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 异构大模型无训练通信优化
tags:
- Multi-Agent
- LLM Communication
- Training-Free
- Symbol Index
- Activation Steering
- Heterogeneous LLM
one_liner: 提出无需训练的异构大模型事实通信接口SYNC，通过共享符号索引+本地向量映射实现跨模型事实传递
practical_value: '- 跨异构LLM Agent通信可复用SYNC的符号索引设计：无需对齐模型架构/训练翻译器，仅通过共享符号表+各模型本地预计算符号方向向量即可实现事实传递，大幅降低多Agent协作的适配成本

  - LLM隐层注入信息优先选相对深度0.2的早期层：实验证实该层写入事实的准确率比中层高65~96个百分点，可直接复用到RAG隐态注入、推荐系统用户偏好注入等场景

  - 多Agent间传递权重类信息可采用隐层写入强度编码：实验显示部分大模型对写入强度的识别准确率比文本打印权重高30+百分点，适合电商推荐兴趣权重、广告出价等数值信息传递

  - 可复用无任务绑定探针提前预测大模型可写入层：无需下游任务数据即可判断各层写入有效性，准确率100%，适合批量适配不同基座的Agent系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent系统要么通过文本通信效率低，要么通过内部状态传递需要训练翻译器或要求模型架构兼容，异构大模型间的低成本高效事实通信一直是痛点，尤其在电商多Agent推荐、广告策略决策等需要多基座协作的场景下，适配成本极高。

### 方法关键点
- 设计SYNC通信框架：通信双方共享固定符号表，发送方将私有事实映射为符号索引传输，无需感知接收方架构或下游任务
- 接收方预计算本地符号方向向量：通过中性词替换后的隐态差值平均得到每个符号在自身隐空间的方向向量，仅需一次前向传播，无需训练
- 事实写入机制：将符号方向向量写入接收方相对深度0.2的早期隐层，复用KV cache实现多轮查询共享写入结果，支持带权重的事实强度编码

### 关键结果
在包含2个世界、4个问答对的选择性事实使用任务上测试，3个不同发送方对接9个不同家族的接收方模型，四答案成功率达72.0%~98.3%，比中层写入最高提升96个百分点，大参数量模型性能与纯文本通信持平；扩展到多token符号的地理知识任务，成功率达23.9%~64.0%，无通信时基线为0%。

最值得记住的一句话：异构大模型间通信不需要对齐内部向量，仅通过共享符号索引+各模型本地的符号表示即可实现无训练的有效事实传递。
