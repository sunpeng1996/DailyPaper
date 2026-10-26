---
title: 'Accordion: Elastic-Depth Inference via Fixed-Prefix Layer Looping'
title_zh: Accordion：基于固定前缀层循环的弹性深度推理MoE模型
authors:
- Yudong Zhang
- Wei Ding
- Kaili Zheng
- Yuchen Ding
- Zhenyu Zhang
affiliations:
- Tsinghua University
- Baidu Inc.
arxiv_id: '2610.32492'
url: https://arxiv.org/abs/2610.32492
pdf_url: https://arxiv.org/pdf/2610.32492
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM弹性推理 · 层循环参数复用
tags:
- Elastic Inference
- Looped Transformer
- MoE
- Inference Optimization
- Multi-Budget
one_liner: 单模型支持5档弹性推理预算，覆盖预训练到RL全链路，效果接近同预算独立专家
practical_value: '- 多场景LLM部署可直接复用弹性深度思路：电商/推荐场景下，低延迟需求的query推荐、搜索suggestion用浅档位，高复杂度的商品文案生成、Agent复杂推理用深档位，无需维护多套模型，大幅降本

  - 训练策略可直接迁移：多档位训练无需额外跨预算一致性损失，每个微批次均匀采样一个预算优化即可，适配LoRA微调、领域适配等场景，训练成本几乎无增量

  - 多领域专家整合方案可复用：通过参数组加权合并+预算匹配的多教师蒸馏，可将多个领域的小专家整合为单弹性模型，适配电商多场景（导购/客服/营销）的统一部署需求

  - 工程实现注意点：层循环的二次attention执行需单独维护KV cache，不同档位的KV存储量随层执行数线性增长，需提前做资源规划'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM应用场景对推理延迟、成本的要求差异极大，单独为每个算力预算训练、维护专用模型会带来极高的研发和部署成本；此前的Looped Transformer方案存在浅路径性能损失问题，且无法适配从预训练到SFT、RL的全链路训练流程。

### 方法关键点
- 架构：基于MoE Transformer，固定中间7-18层为可循环窗口，5档推理预算分别循环窗口的前0/3/6/9/12层，零初始化残差门控控制二次执行的输出，所有档位共享权重，仅新增极少量门控参数
- 训练：预训练每个微批次均匀采样一个预算，仅优化对应路径的下一词预测损失，无需额外跨预算一致性损失；SFT阶段延续相同采样策略；RL阶段先训练3个分领域（指令/数学/代码）的弹性专家，再通过参数组合并+预算匹配多教师蒸馏整合为单模型
- 推理：每请求固定选择一档预算，二次执行的attention单独维护KV cache，不同档位FLOPs线性增长，无权重冗余

### 关键结果
- 6B-A0.5B模型预训练3.6T token后，推理深度从最低档到最高档，37项任务的5类平均得分提升3.01个百分点，中间档（k=6）仅用一半的额外层执行量就能拿到89%的收益
- 各档位效果和单独训练的同预算专家模型损失差小于0.003 nats，RL后模型在对应领域的任务-预算平均得分超过单领域专家
- 长上下文场景下弹性深度收益更明显，32K上下文时最高档比最低档RULER得分高5.47个百分点

最值得记住的一句话：单模型弹性深度是平衡LLM应用效果、成本、延迟的高性价比路径，无需额外一致性损失的均匀采样训练策略即可实现多档位效果接近独立专家。
