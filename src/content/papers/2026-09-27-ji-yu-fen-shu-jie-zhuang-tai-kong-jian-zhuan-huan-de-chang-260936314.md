---
title: Fractional State Space Transition for Long Sequence Modeling
title_zh: 基于分数阶状态空间转换的长序列建模方法
authors:
- Ivan Kobyzev
- Abbas Ghaddar
- Ali Nasiri-Sarvi
- Lifeng Shang
- Yufei Cui
affiliations:
- Huawei Noah’s Ark Lab, Montreal Research Center
arxiv_id: '2609.36314'
url: https://arxiv.org/abs/2609.36314
pdf_url: https://arxiv.org/pdf/2609.36314
published: '2026-09-27'
collected: '2026-10-01'
category: LLM
direction: 长序列建模 · 分数阶SSM
tags:
- SSM
- Long-Context
- Fractional-Dynamics
- Sequence-Modeling
- Mamba
one_liner: 将分数阶动力学引入SSM，用对数间隔指数模态近似幂律核，兼顾长短序列建模性能
practical_value: '- 长序列用户行为建模场景可参考FRAC的幂律记忆设计，替换现有Mamba的指数衰减核，提升久远用户行为（如3个月前的浏览、购买记录）的特征保留能力，优化长周期兴趣召回效果

  - 对数间隔多指数模态的近似方法可直接复用，在不增加过多计算量的前提下扩展记忆时长，适配推荐系统动辄上千的用户行为序列长度需求

  - 多时间尺度的读写权重设计可借鉴到用户兴趣分层建模，不同时间尺度的记忆模态对应短/中/长期兴趣，单独做读写控制提升兴趣建模精度

  - 推理阶段和现有SSM完全兼容，支持bounded state autoregressive decoding，无需修改现有推理部署框架，可直接替换Mamba模块做AB实验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主流SSM（如Mamba系列）基于ODE动力学，天然带指数遗忘特性，长上下文下久远信息保留能力差；而真实场景中，无论是长文档理解还是推荐系统的长用户行为序列，早期信息往往仍有不可忽略的作用。分数阶微分方程可描述幂律长记忆，但原有实现是非马尔可夫的，无法直接适配有限状态循环计算，落地难度极高。
### 方法关键点
- 提出FRAC架构，将分数阶动力学的幂律核用有限个对数间隔的指数模态加权和近似，转化为有限状态的马尔可夫循环结构
- 每个模态对应不同时间尺度，通过token依赖的分数阶参数α、尺度参数λ、读写权重实现选择性记忆，完全保留SSM并行训练、prefill能力，以及有限状态自回归解码特性
- 基于分数阶核的渐近特性设计读权重的对数时间尺度先验，提升信息读写的对齐效率
### 关键实验结果
- 合成重尾探测任务：仅用长度512序列训练，128K长度下准确率比Mamba3高7pct，远优于仅能支持8K以内的原生Attention
- 1.3B参数LLM预训练：LongBench平均得分比最强SSM baseline GDN高1.9%，8/14任务最优；NIAH任务64K长度下性能衰减比Mamba3慢20%以上；短上下文LM Harness性能和Transformer仅差0.2%
- DNA序列建模：64K长度下perplexity比Mamba3低2%左右
### 最值得记住的结论
将SSM的指数遗忘替换为幂律遗忘，可在几乎不损失短序列性能、不增加推理成本的前提下，大幅提升长序列建模的泛化能力。
