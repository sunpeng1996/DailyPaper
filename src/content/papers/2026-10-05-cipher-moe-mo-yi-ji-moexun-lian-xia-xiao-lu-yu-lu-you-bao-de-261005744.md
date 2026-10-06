---
title: 'CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE
  Training'
title_zh: 《CIPHER-MoE：万亿级MoE训练下效率与路由保真性的平衡方案》
authors:
- Jing Li
- Jian Meng
- Yingmeng Gao
- Suming Qiu
- Linyuan Qiu
- Dongfang Li
- Baotian Hu
- Binfan Zheng
- Rongqian Zhao
- Weijian Sun
affiliations:
- Tongji University
- Cornell University
- Harbin Institute of Technology, Shenzhen
- Shenzhen Loop Area Institute AI Training Platform Team
arxiv_id: '2610.05744'
url: https://arxiv.org/abs/2610.05744
pdf_url: https://arxiv.org/pdf/2610.05744
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 大模型训练 · MoE负载均衡优化
tags:
- MoE
- LLM Training
- Load Balancing
- Workload Optimization
- Trillion Parameter Model
one_liner: 提出不修改原有Top-K路由的轻量MoE负载均衡算法，实现1.1-1.94倍训练加速且不损模型质量
practical_value: '- 电商/推荐场景做域专属MoE大模型SFT时，无需改造复杂的系统级专家迁移/复制逻辑，直接嵌入CIPHER-MoE的专家侧相似度过滤+容量控制模块，即可解决训练OOM、速度慢的问题，适配现有训练框架的成本极低

  - MoE域微调时优先选择strict token drop而非token reroute策略，可避免干扰专家已有的专业化特征，训练速度更快且模型效果更优

  - 若使用的MoE模型参数量低于300B，CIPHER-MoE的加速增益不到5%，优先在200B以上的大参数量MoE训练场景落地ROI最高

  - 可以复用其推导的专家最小容量边界公式，按需动态调整每个专家的batch处理上限，进一步降低硬件资源浪费'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
万亿级MoE训练存在严重的专家负载不均衡问题，实际域SFT场景下10%的专家会承担88%的路由流量，既会导致硬件利用率低、训练速度慢，还容易触发OOM直接训练失败；现有方案要么是系统级的专家迁移/复制，实现复杂度高额外开销大，要么是路由正则化，会破坏专家专业化降低模型质量，缺乏兼顾效率、效果、落地成本的方案。
### 方法关键点
- 不修改原有Token侧Top-K路由逻辑，新增专家侧双向过滤：每个专家按token与门控向量的余弦相似度排序，仅保留容量阈值内最高相似度的token，超出的直接丢弃
- 理论推导了专家保留有效训练信号所需的最小容量边界，保证过滤后不会丢失关键梯度信息
- 对比token reroute和strict drop两种溢出处理策略，验证strict drop效果更优，不会干扰专家已有的专业化特征
- 新增KL散度locality loss，引导token优先路由到同EP组的本地专家，降低跨节点通信开销
### 关键实验结果
在284B~1.6T的4个主流大MoE（DeepSeek-V3/V4、GLM-5）上测试，覆盖运筹、医疗、社交常识三类域SFT数据集，对比vanilla MoE、LocMoE、固定路由三类基线：最高降低64.9%的Top1专家负载，实现1.10×~1.94×的训练加速，域任务效果平均提升0.5~1pct，通用能力无损失；可让原本直接OOM的1.6T DeepSeek-V4-Pro顺利启动训练。
> 最值得记住的一句话：MoE负载均衡不需要复杂的系统调度，仅通过专家侧基于相似度的容量控制，就能在不修改原有路由逻辑、不损失模型质量的前提下实现近2倍训练加速
