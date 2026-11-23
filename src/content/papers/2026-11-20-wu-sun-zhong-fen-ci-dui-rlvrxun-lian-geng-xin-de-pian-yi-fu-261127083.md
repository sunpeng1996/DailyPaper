---
title: How Far Does Lossless Re-tokenization Move an RLVR Update?
title_zh: 无损重分词对RLVR训练更新的偏移幅度量化研究
authors:
- Zhe Dong
- Fang Qin
affiliations:
- University of Maine at Presque Isle
- Stanford University
arxiv_id: '2611.27083'
url: https://arxiv.org/abs/2611.27083
pdf_url: https://arxiv.org/pdf/2611.27083
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 大模型RL训练 · 重分词漂移量化
tags:
- RLVR
- tokenization
- reinforcement learning
- LLM training
- gradient drift
one_liner: 量化无损重分词导致的RLVR训练更新偏移幅度，证明重加权无法彻底消除该偏差
practical_value: '- 做电商导购Agent、广告文案生成Agent、生成式推荐模型的RLVR/RLHF调优时，必须保留采样得到的原始token ID贯穿全pipeline，不要解码成文本再重编码，可有效降低训练波动

  - 若业务需跨模块传递文本（如Agent工具调用结果拼接后训练），优先对每个分段单独分词，不要整段联合分词，可将重分词影响的token占比控制在0.0003以下，几乎不影响训练效果

  - 用LoRA做RL微调时，重分词导致的更新偏移是全参数微调的1.5倍左右，基于LoRA的业务调优场景需更严格规避重分词操作

  - 训练batch规模大于100条时，重分词的偏移影响会被放大，此时必须严格执行Token-In-Token-Out（TITO）规范'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLVR是当前大模型Agent、生成式推荐模型对齐的核心技术，工业界仅指出重分词漂移是训练不稳定的潜在来源，从未量化其对更新的实际影响，也不清楚是否能通过重加权消除该偏差，缺乏可落地的pipeline设计依据。

### 方法关键点
- 设计配对单更新测量范式：从同一起始checkpoint，分别对同一批rollout的原始分词版本、人为拆分部分token的无损重分词版本做训练更新，计算两个更新的归一化距离c
- 引入替换batch的更新距离作为参照，定义偏移比R=重分词偏移距离/换batch偏移距离，R=1代表重分词的影响和更换整批数据相当
- 覆盖4款主流开源模型，在三位数加法、GSM8K两个任务上测试，对比LoRA/全参数微调、5种代理损失函数的表现
- 构造表格模型从理论上证明重加权是否能消除偏差

### 关键实验数字
- 每25个token拆分1个时，R=0.556，即重分词的偏移幅度相当于更换半批数据；拆分最早出现的可拆分token时，偏移是拆分最晚出现的1.65倍
- LoRA微调下的R是全参数微调的1.5倍，所有5种损失函数都无法消除重分词偏移
- 真实pipeline中无损重分词仅影响最多5.2%的rollout，仅0.08%的token，远低于实验测试的最小拆分比例
- GSM8K训练实验中，保留原始token的实验组在14/18的配对测试中准确率更高，平均准确率高1.6个百分点

### 最值得记住的一句话
Agent/生成式模型RL训练中，只要文本不变就不影响训练的认知是完全错误的，仅0.03比例的token分词变化就能带来相当于换半批数据的更新偏移
