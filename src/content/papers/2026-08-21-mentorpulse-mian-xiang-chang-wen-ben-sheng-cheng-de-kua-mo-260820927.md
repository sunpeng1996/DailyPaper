---
title: 'MentorPulse: Refreshing Cross-Model Latent Guidance for Long-Form Generation'
title_zh: MentorPulse：面向长文本生成的跨模型隐态引导动态刷新框架
authors:
- Ziwu Liu
- Guozhong Li
- Chen Qiu
- Weiyang Kong
- Panos Kalnis
affiliations:
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2608.20927'
url: https://arxiv.org/abs/2608.20927
pdf_url: https://arxiv.org/pdf/2608.20927
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: 大小模型协作 · 长文本生成优化
tags:
- Cross-Model-Guidance
- Long-Form-Generation
- Latent-Representation
- KV-Cache
- Efficient-Inference
one_liner: 提出跨模型动态刷新隐态引导机制，低成本让小模型大幅缩小与大模型的长文本生成能力差距
practical_value: '- 电商长文案（商品详情、直播脚本）生成可复用该大小模型协作架构：大模型做引导、小模型生成，每16~32 token刷新一次隐态，既降本又避免长文本跑题

  - 复用槽位内存压缩+增量刷新设计：跨模型交互仅传2.7~10.6MB压缩隐态，大幅降低边缘端小模型与云端大模型的通信开销

  - 可借鉴V64读分布方差指标，上线前快速筛选大小模型配对效果，避免无效调试

  - 窗口刷新训练（WRT）可迁移至多轮客服对话生成等动态上下文场景，无需重置KV cache即可适配上下文变化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有跨模型隐态引导方法仅在生成前计算一次大模型（导师）的引导信号，长文本生成时信号会随生成内容迭代逐渐过时，反而让小模型（学生）生成质量低于无引导基线；而长文本场景是大小模型协作降本的核心场景，亟待解决引导失效问题。
### 方法关键点
- 槽位内存构造：将导师模型隐态压缩为固定大小的位置感知槽位内存，保留最新32个token的原始状态，更早内容按32token分段取末尾状态，传输量仅为完整KV cache的1%左右
- 增量刷新机制：默认每16个token仅将学生新生成的token传给导师增量计算隐态，热更新内存时不修改学生的KV cache，不中断生成流程
- 窗口刷新训练（WRT）：训练跨注意力桥接层时随机采样刷新边界，让模型适配引导信号的动态变化，初始门控设为0保证兼容原生小模型
### 关键结果
在13个数据集、11组大小模型配对上测试，MentorPulse平均缩小52.2%的大小模型能力差距，性能远超同参数预算的LoRA、静态引导C2C等方案；长文本生成场景下静态引导会让效果比纯学生低1.7~5.1个百分点，MentorPulse完全逆转该退化，同时每请求成本比刷新文本引导的方案低41~54倍。
> 最值得记住：长文本生成场景下静态跨模型引导必然过时，16token间隔的低成本隐态刷新是兼顾效果和成本的最优区间
