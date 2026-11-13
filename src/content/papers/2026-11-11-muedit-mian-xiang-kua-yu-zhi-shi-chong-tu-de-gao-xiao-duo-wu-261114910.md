---
title: 'MuEdit: An efficient multi-task editing method towards inter-domain knowledge
  conflicts'
title_zh: MuEdit：面向跨域知识冲突的高效多任务LLM编辑方法
authors:
- Songshi Liang
- Ting-En Lin
- Zixuan Huang
- Yuchuan Wu
- Yongbin Li
- Zihe Wang
- Rui Yan
affiliations:
- 中国人民大学高瓴人工智能学院
- 阿里巴巴集团
- 北京航空航天大学
- 武汉大学人工智能学院
- 武汉大学计算机学院
arxiv_id: '2611.14910'
url: https://arxiv.org/abs/2611.14910
pdf_url: https://arxiv.org/pdf/2611.14910
published: '2026-11-11'
collected: '2026-11-13'
category: LLM
direction: 大语言模型 · 多任务知识编辑
tags:
- Model Editing
- Multi-task Learning
- Null-space Projection
- Low-rank Approximation
- LLM
one_liner: 提出Conflict Index量化跨任务冲突，结合排序与动态低秩逼近解决LLM多任务编辑遗忘问题
practical_value: '- 多任务SFT/模型迭代场景可复用Conflict Index量化不同任务的参数空间冲突，优化训练顺序，大幅降低跨任务遗忘

  - 电商/客服LLM同时更新商品知识、安全规则、服务话术等多域知识时，可采用动态低秩压缩高冲突任务的保留矩阵，在极小性能损失下扩大可更新空间

  - 增量任务接入场景可复用Greedy Order策略，无需回溯历史训练过程，性能接近最优排序效果且计算成本极低

  - Conflict Index计算仅需每个域最低50条参考样本，无需完美域边界，适配小样本业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM单域顺序编辑方法在跨多任务域（常识、安全、QA、情感、多语言等）迭代时会出现严重灾难性遗忘，根源是不同域的保留表示null-space不对齐，公共可更新子空间过小，新编辑极易覆盖旧有知识。
### 方法关键点
1. 提出Conflict Index量化不同任务null-space的重叠度，取值0~1，数值越高代表跨任务更新冲突越强
2. 冲突感知排序：离线场景全局搜索最优任务顺序最小化相邻冲突；在线增量场景用Greedy Order将新任务插入到最小冲突位置，仅用局部窗口做null-space投影，无需回溯历史编辑
3. 动态低秩逼近：当任务对冲突超过自适应阈值时，对整体冲突更高的任务的保留矩阵做SVD压缩，扩大公共null空间，压缩比例随冲突程度自适应调整
### 关键实验
在Llama3-8B、Qwen2.5-7B、GPT2-xl三个骨干，跨5个功能域验证，对比ROME、MEMIT、AlphaEdit、AnyEdit等SOTA基线：最优排序下Mu-Edit的ZsRE特异性从AnyEdit的0.7098提升到0.8845，CKnowEdit特异性从0.6882提升到0.8505；Greedy Order性能仅比最优排序低0.014以内，排序成本下降数个数量级；仅需50条参考样本即可稳定计算Conflict Index，性能无骤降。
### 核心结论
跨任务编辑的遗忘根源不是更新量过大，而是不同域null-space的几何不兼容，优先调整任务顺序减少冲突，效果远优于强制约束更新量
