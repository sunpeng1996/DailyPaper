---
title: Attention-Path Fragility as an Uncertainty Signal in Large Language Models
title_zh: 基于注意力路径脆弱性的大语言模型不确定性估计方法
authors:
- Minsoo Kim
- Sungyoung Ji
- Kisung Moon
- Ilyong Yoon
affiliations:
- POSCO Holdings Future Technology Research Institute
arxiv_id: '2608.11138'
url: https://arxiv.org/abs/2608.11138
pdf_url: https://arxiv.org/pdf/2608.11138
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM 不确定性评估 · 注意力路径扰动
tags:
- Uncertainty Estimation
- Attention Head
- Hallucination Detection
- Grounded QA
- Training-free
one_liner: 提出无需训练的ASMI算法，通过注意力头掩蔽探测路径脆弱性，在上下文路由QA任务上优于主流不确定性基线
practical_value: '- 做RAG问答类Agent的幻觉检测时，可直接复用Sem-ASMI方案，仅需贪心输出+40次注意力头掩蔽推理，无需额外训练，长上下文RAG场景下比语义熵基线成本低27%，还能额外捕捉置信度高但错误的输出

  - 电商商品咨询、售后大模型服务的选择性输出场景，可在原有置信度过滤基础上叠加ASMI脆弱性信号，对高置信输出做二次校验，可将保留错误率降低约50%

  - 当大模型输出依赖参数记忆而非RAG上下文时，不要用ASMI，直接用MSP等零成本输出置信度基线即可，避免不必要的推理开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM不确定性估计方法存在明显短板：多采样类方法（如语义熵）需要生成数十个候选，推理成本高；单步置信度类方法仅依赖输出分布，无法识别「高置信但依赖单一脆弱注意力路径」的错误，这类错误在RAG、智能客服等上下文路由场景中占比高、业务损失大，亟需低成本且能捕捉内部路径依赖的不确定性信号。

### 方法关键点
- 提出ASMI（注意力子网络互信息）：推理时随机掩蔽Transformer中间层的注意力头，计算不同掩蔽子网络输出分布的BALD互信息，量化路径脆弱性，无需训练微调
- 加入语义一致性核：基于输出层嵌入的余弦相似度对同义候选的差异做衰减，避免将表面形式不同的语义等价输出误判为不确定性
- 工程优化：目标层以下的前缀计算仅做1次缓存，仅重复计算目标层以上的后缀，大幅降低多轮掩蔽的推理开销

### 关键结果
在4个主流LLM骨干（Qwen3-4B/8B、Llama2-7B、Mistral-7B）上测试：12个上下文路由QA（CoQA、SQuAD、BabiQA）组合中，无采样的Sem-ASMI在10个上打平或优于需要10次采样的语义熵基线；在高置信输出区间，叠加ASMI信号可将保留错误率降低约50%；在闭卷参数记忆任务（TriviaQA）上ASMI效果退化为与零成本MSP基线相当，完全符合设计预期。

> 最值得记住：不确定性信号的适用范围可预测，ASMI仅在输出依赖上下文注意力路由的场景有增益，参数记忆场景优先用零成本输出置信度基线
