---
title: Virtual Head Attention
title_zh: 虚拟头注意力（VHA）：打破注意力机制不可能三角
authors:
- Xibo Ding
- Guoxia Wang
- Jinle Zeng
- Jiabin Yang
- Sirui Tao
- Chao Yang
- Dianhai Yu
affiliations:
- Baidu Inc.
- Peking University
arxiv_id: '2610.17959'
url: https://arxiv.org/abs/2610.17959
pdf_url: https://arxiv.org/pdf/2610.17959
published: '2026-10-12'
collected: '2026-10-16'
category: LLM
direction: LLM注意力优化 · KV缓存压缩
tags:
- Attention Mechanism
- KV Cache
- GQA
- Long Context LLM
- Reparameterization
- MoE
one_liner: 通过两个可推理折叠的线性操作，在兼容GQA的前提下同时优化KV缓存、训练FLOPs与模型质量
practical_value: '- 生成式推荐、电商客服Agent、商品文案生成等场景的中小参数LLM，可直接将原有GQA替换为VHA，无需修改vLLM/SGLang等推理框架，即可获得2~4倍KV缓存压缩、7%~8%训练FLOPs下降，同时模型质量不降反升，大幅提升服务并发、降低推理成本

  - VHA的训练-推理解耦重参数范式可直接迁移到推荐系统场景：训练时添加近恒等初始化的纯线性正则化分支，推理时完全折叠进原有投影矩阵，零额外推理开销，可用于平衡双塔、多兴趣建模等模块的训练效果与推理速度

  - 需处理长上下文的电商全会话理解、用户长周期行为建模LLM，采用VHA可在128K上下文下维持比GQA高11.4的RULER平均分，同时KV缓存减半，有效降低长序列推理的内存开销与延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM的注意力机制长期存在「不可能三角」约束：KV缓存大小、训练/预填充FLOPs、模型质量三者无法同时优化。主流GQA-8方案质量高但KV缓存开销大；MLA可压缩缓存但质量损失明显；MFA缓存占用低但训练/预填充FLOPs提升近50%，无方案能同时实现三者最优。
### 方法关键点
- 仅引入两个无非线性的轻量线性操作：Q Premix对每个KV组内的query做近恒等线性变换，将减半的物理query头扩展为虚拟头，恢复注意力多样性；Linear Postmix通过低秩`I+AB⊤`残差结构融合头间特征
- 两个模块均为纯线性操作，推理时可分别折叠进query投影和输出投影矩阵，完全退化为标准GQA-2架构，100%兼容现有GQA推理优化（vLLM、SGLang等）
- 仅保留2个KV头，大模型下组大小可达64，可充分利用Tensor Core并行算力
### 关键结果
- 0.6B~8B MoE规模4K上下文预训练下，VHA较GQA基线精度提升0.05%~0.81%，稠密模型KV缓存较GQA-8压缩4倍，MoE模型较GQA-4压缩2倍，1.7B规模下训练/预填充FLOPs下降7.9%
- 工业级30B MoE 8K上下文500B token预训练下，VHA较MLA、GQA-4在12个基准测试集上平均精度分别提升0.7%、2.6%
- 10B MoE长上下文训练后，8K~128K上下文下VHA的RULER平均得分84.4，远超GQA的73.0
### 核心结论
通过训练时重参数、推理时折叠的纯线性结构设计，可以在完全兼容现有推理栈的前提下，打破注意力机制的不可能三角
