---
title: Fault-tolerant foundation models
title_zh: 容错基础模型
authors:
- Trevor McCourt
- Ila R. Fiete
- Isaac L. Chuang
affiliations:
- Massachusetts Institute of Technology (MIT)
arxiv_id: '2610.10311'
url: https://arxiv.org/abs/2610.10311
pdf_url: https://arxiv.org/pdf/2610.10311
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: 大模型训练 · 硬件容错优化
tags:
- LLM
- Fault Tolerance
- Scaling Law
- Energy Efficiency
- Hardware Aware Training
one_liner: 通过4万GPU时实验验证，训练时注入硬件故障的LLM随规模增大容错性提升，可适配低能耗硬件
practical_value: '- 大流量LLM落地场景（如电商推荐的LLM重排序、Agent生成个性化文案）可复用故障感知训练范式，配合低功耗硬件，大幅降低推理端能耗成本，百万QPS级场景成本下降可达数倍

  - 训练时按概率注入块级置零扰动的思路，可迁移到LLM4Rec的鲁棒性训练中，提升模型对INT4/INT2量化、分布式推理节点故障的容忍度，减少线上SLA故障

  - 可复用「模型规模越大容错能力越强」的结论，在推荐/Agent场景落地超大规模LLM时，可采用更极致的压缩、KV cache截断等优化，不用过度担心微小故障对效果的影响'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前AI推理能耗极高，商用硬件为保证运算可靠性需运行在高电压下，门电路能耗随电压平方增长；低能耗的模拟、低压数字、光子、神经形态硬件都存在随机运算故障，但常规训练的LLM对故障极敏感，甚至4比特量化都会显著降低效果，破解该矛盾可实现LLM部署成本数量级下降。

### 方法关键点
- 故障感知训练范式：训练和推理时注入相同的硬件故障模拟，在attention、FFN的矩阵运算中按概率p随机将4个连续元素块置零，模拟带错误检测的低功耗硬件的故障模式
- 推导故障硬化模型的改进缩放定律，在常规Chinchilla缩放定律基础上新增曲率项α₂，解释大模型规模超过临界值后容错能力回升的规律
- 用相对容量η/N（故障硬化模型等效的无故障模型参数量/自身参数量）衡量容错效率，值越高代表纠错冗余开销越低

### 关键实验结果
基于3500亿token的FineWeb数据集训练7.9M~9.3亿参数量的Llama2风格模型，累计消耗4万GPU时：
1. 故障感知训练的模型规模超过临界值N*后，η/N随规模上升持续提升，符合「好」纠错码的特征，冗余开销不随规模升高
2. 当推理故障概率p≤训练时的p值时，故障硬化模型输出logit几乎无漂移，容量损失<5%；常规无故障训练的模型在p=0.1时容量损失超60%，甚至会出现训练数据越多效果越差的反规模效应

### 核心结论
大模型在故障环境下训练会自发学习类似大脑网格细胞的分布式纠错码，未来有望在低功耗故障硬件上实现数量级的推理能耗下降
