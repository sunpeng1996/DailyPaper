---
title: 'LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation'
title_zh: LatentLoop：面向循环MoE的非对称计算分配扩展方法
authors:
- Zefeng He
- Yunkai Chai
- Xiaoyang Chen
- Tong Zhu
- Zongliang Wu
- Yun Luo
- Yafu Li
- Yu Cheng
affiliations:
- SJTU
- Shanghai AI Lab
- USTC
- CUHK
- NTU
arxiv_id: '2610.19975'
url: https://arxiv.org/abs/2610.19975
pdf_url: https://arxiv.org/pdf/2610.19975
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: 循环MoE · 非对称算力分配
tags:
- MoE
- Looped Transformer
- Compute Efficiency
- Asymmetric Allocation
- Sequence Compression
one_liner: 发现循环MoE两次访问的残差非对称特性，通过首访压缩+算力重分配提升训练与下游性能
practical_value: '- 业务自研小参数量MoE/循环Transformer时，可复用非对称算力分配思路：对前几层/首趟循环降低计算量（如序列压缩、减少激活专家数），节省的算力倾斜给后续贡献更大的层/后趟循环，总预算不变即可提升模型效果

  - 循环共享参数场景下，可参考选择性参数共享策略：占参比高的模块（如MoE专家、召回侧item embedding层）跨循环共享，占参小、对输入特征敏感的模块（如Attention、用户行为编码层）单独设计，平衡参数量开销与效果

  - 多轮迭代的Agent推理链路可借鉴残差非对称结论：前几轮推理设置更低的残差更新权重，降低无效更新开销，后几轮设置更高权重保障推理精度，总推理预算不变下提升任务表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped MoE通过共享参数提升有效深度，兼顾参数效率与稀疏计算优势，但现有对称计算分配未考虑不同循环访问的贡献差异，固定预算下无法最大化性能。之前研究发现不同循环访问的作用存在区别，但未深入探索算力分配的优化空间，亟需在不增加参数、KV cache、单步FLOPs、总训练FLOPs的前提下，进一步提升Looped MoE的效率与效果。

### 方法关键点
- 验证残差系数非对称特性：两次循环访问的最优残差更新系数差异显著，首访系数可降至0.25不损失效果甚至提升，次访系数降低则验证NLL明显上升
- 首访序列压缩：对第一次循环的输入序列做2倍均值压缩，仅在压缩后的隐序列上执行计算，节省的算力重分配给模型宽度，提升整体表征能力
- 校准回写机制：引入通道级可学习回写系数，控制首访压缩计算得到的更新量写回全分辨率序列的强度，仅新增2d参数，复杂度极低
- 选择性参数共享：跨两次循环共享占参比最高的MoE路由与专家权重，仅对分辨率敏感的Attention模块单独设置参数，通过微调存储专家数抵消新增参数开销，总参数量保持不变

### 关键结果
在1.3B-7B共15组严格匹配预算的配置下训练，训练算力最高达10^21 FLOPs，对比baseline为普通MoE、对称循环MoE（SMELT）：
- 相同验证NLL（1.988）下，训练算力比普通MoE节省19.0%，比对称循环MoE节省7.9%
- 9个下游基准测试上，0-shot、5-shot所有尺寸下平均得分均为最高，5-shot下比对称循环MoE最高提升1.18个百分点

### 核心结论
循环架构中不同轮次的贡献天然存在不对称性，不必给每一轮分配均等的计算资源，针对性倾斜算力可以在零额外预算下实现效果与效率的双重提升
