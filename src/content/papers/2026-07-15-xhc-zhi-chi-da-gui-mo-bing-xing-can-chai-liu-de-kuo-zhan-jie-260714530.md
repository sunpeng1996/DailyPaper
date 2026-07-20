---
title: 'xHC: Expanded Hyper-Connections'
title_zh: xHC：支持大规模并行残差流的扩展超连接架构
authors:
- Xiangdong Zhang
- Xiaohan Qin
- Sunan Zou
- Tuo Dai
- Xiaoming Shi
- Huaijin Wu
- Yebin Yang
- Zhuo Xia
- Shaofeng Zhang
- Lin Yao
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- University of Science and Technology of China
- Peking University
- The Chinese University of Hong Kong
arxiv_id: '2607.14530'
url: https://arxiv.org/abs/2607.14530
pdf_url: https://arxiv.org/pdf/2607.14530
published: '2026-07-15'
collected: '2026-07-20'
category: Training
direction: LLM预训练 · 残差流扩展架构优化
tags:
- MoE
- Transformer
- Residual Stream
- Scaling Law
- Training Efficiency
one_liner: 突破HC类方法N≤4限制，实现N=16残差流扩展，大幅提升MoE大模型训练效率与效果
practical_value: '- 自研业务侧LLM（电商文案生成、Agent推理大模型等）时，可复用xHC稀疏残差流设计，仅增加少量训练FLOPs即可提升模型效果，性价比高于直接堆参/堆深度。

  - 序列建模优化时，可借鉴时序特征增强思路，用轻量因果卷积补充相邻token上下文，无需成倍增加层FLOPs就能丰富残差写回信息，适配召回/推理场景。

  - 工程落地可复用xHC-Flash的跨子层计算共享、算子融合策略，大幅降低多流残差架构的内存访问开销，控制训练/推理延迟满足线上要求。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有HC类残差流扩展方法最多支持N=4并行流，超过该值后性能收益边际递减，训练成本随N呈三次方上升，无法成为和宽度、深度并列的LLM规模化扩展维度，亟需突破该瓶颈。

### 方法关键点
- 针对写回信息不足瓶颈：引入时序特征增强，对MLP输出做多尺度因果卷积提取相邻token特征，经Gram-Schmidt正交化后扩充写回信号维度，避免多流冗余。
- 针对计算瓶颈：设计非对称稀疏残差架构，仅激活k=4个流做残差混合与写回，保留全量流的读权限，将残差映射生成成本从O(N³C)降至O(k³C)。
- 配套落地优化：推出xHC-Flash，通过跨子层共享路由、预映射计算，配合算子融合将内存访问开销降至接近N=4的mHC水平。

### 关键结果数字
- 18B MoE模型上，xHC平均下游得分48.8，比mHC高4.0分，仅比vanilla基线多4.1%训练FLOPs；达到相同损失时，vanilla需要1.5×、mHC需要1.19×于xHC的计算量。
- xHC-Flash（N=16，k=4）单子层内存流量40C，仅比N=4的mHC的34C高17.6%，保留99%以上的xHC性能收益。

### 核心结论
残差流扩展是完全独立于宽度、深度的全新LLM规模化维度，xHC让N≥4的扩展首次具备落地性价比。
