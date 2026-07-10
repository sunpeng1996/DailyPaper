---
title: Any-Dimensional Learning by Sampling
title_zh: 基于随机采样的任意维度学习方法
authors:
- Eitan Levin
- Venkat Chandrasekaran
affiliations:
- University of Chicago
- California Institute of Technology
arxiv_id: '2607.07680'
url: https://arxiv.org/abs/2607.07680
pdf_url: https://arxiv.org/pdf/2607.07680
published: '2026-07-08'
collected: '2026-07-10'
category: Training
direction: 可变尺寸输入模型的跨尺寸泛化与速写
tags:
- generalization
- random_sampling
- sketching
- variable_length_input
- transformer
- gnn
one_liner: 提出基于随机采样映射的统一框架，解决可变尺寸输入模型的跨尺寸泛化与大输入速写问题
practical_value: '- 电商推荐场景中用户行为序列长度差异大，可复用文中随机采样映射方法，用短序列训练的模型泛化到长序列推理，降低训练算力成本

  - 处理超大输入（如超长用户行为序列、大规模商品关联图谱）时，可借鉴文中速写策略，在效果损失可控的前提下大幅降低推理延迟

  - 部署排列不变Transformer做用户兴趣建模时，可参考文中给出的泛化率边界，量化跨长度泛化效果上限，指导训练数据长度分布设计'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前大量ML模型适配可变尺寸输入（如不同长度文本/行为序列、不同节点数图）时存在两大核心痛点：一是小尺寸输入训练得到的模型无法稳定泛化到训练阶段从未见过的大尺寸输入；二是大尺寸输入推理计算成本过高，缺乏统一的小尺寸近似方法。
### 方法关键点
提出基于随机采样映射的统一框架，覆盖有放回采样、随机分箱、物种采样三类通用采样方法，根据不同领域不同尺寸问题实例的对称性与关联关系，匹配对应适用的采样类型。
### 关键结果
针对序列、图、张量等多类可变尺寸输入的函数族（包含排列不变Transformer、GNN等常用模型），给出了明确的泛化速率与速写速率边界，可直接指导可变尺寸输入模型的训练与推理优化。
