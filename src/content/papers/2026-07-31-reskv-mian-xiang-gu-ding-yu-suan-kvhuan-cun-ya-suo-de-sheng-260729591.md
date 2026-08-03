---
title: 'ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV
  Cache Compression'
title_zh: ResKV：面向固定预算KV缓存压缩的省略注意力贡献重构方法
authors:
- Yuhang Zhan
- Lisi Chen
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2607.29591'
url: https://arxiv.org/abs/2607.29591
pdf_url: https://arxiv.org/pdf/2607.29591
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: LLM推理 · KV缓存压缩
tags:
- KV Cache
- Long-Context Inference
- Inference Optimization
- Transformer
- Model Compression
one_liner: 提出固定KV预算拆分为精确主缓存+残差缓存的压缩方案，同等内存下大幅提升长上下文推理效果
practical_value: '- 做Agent长上下文推理时，可直接集成ResKV替换现有KV缓存策略，在不增加显存占用的前提下提升长prompt（如用户历史行为、多轮对话、商品库召回结果）的理解准确率，尤其适合预算紧张的在线服务场景

  - 主缓存+残差的设计思路可迁移到推荐系统的用户行为序列建模：高优先级行为（如点击、购买）存精确特征，低优先级行为（如曝光、浏览）聚合为残差特征，在特征存储预算固定时提升序列建模效果

  - 动态门控trick可复用：当主注意力分布足够尖锐时抑制残差贡献，避免低价值信息干扰核心需求匹配，适合推荐排序、LLM精准召回场景

  - ResKV的分层/分头残差预算分配策略，可直接用于现有大模型推理服务部署，无需重新训练模型即可获得性能提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理的KV缓存随序列长度线性增长，是显存和带宽的主要消耗源。现有KV压缩方法要么直接丢弃低优先级token丢失聚合注意力贡献，要么合并token扰动保留的精确KV，两者都无法在固定预算下同时兼顾精确记忆保留和省略信息的贡献还原，尤其在query-agnostic（压缩时不知道后续查询）的真实部署场景下精度损失严重。

### 方法关键点
1. 缓存拆分：固定KV预算拆分为m个精确主缓存槽+ r个残差缓存槽，主缓存存高优先级token的原始KV，残差缓存用聚类聚合省略token的均值K、均值V和群体数量，不修改主缓存的精确值
2. 共享softmax解码：主缓存token和残差条目参与同一个softmax计算，残差同时贡献注意力的分子和分母权重，而非事后校正，还原省略token的聚合注意力贡献
3. 自适应残差控制：构造阶段用验证代理为每层/每个KV头选择最优残差预算，只有残差能降低注意力重建误差时才分配；解码阶段用动态门控，根据主缓存注意力的尖锐度自动调节残差权重，主注意力足够集中时抑制残差避免干扰

### 关键结果
在LongBench（16个长上下文任务）和RULER（13个可控长上下文测试）上测试，覆盖LLaMA-3.1-8B、Qwen-2.5-7B两个骨干，对比H2O、SnapKV、AdaKV等主流压缩基线：同等KV预算下，ResKV提升全部32个LongBench配置、63/64个RULER配置的效果，平均在LongBench涨1.02点，RULER涨3.38点，query-agnostic场景下平均涨4.54点，显存开销几乎无增加，128K上下文下吞吐量仍保持稳定。

**最值得记住的一句话**：KV缓存压缩不是非存即删的二元选择，将省略token的聚合贡献作为独立残差保留，即可在不增加显存预算的前提下大幅提升长上下文推理效果。
