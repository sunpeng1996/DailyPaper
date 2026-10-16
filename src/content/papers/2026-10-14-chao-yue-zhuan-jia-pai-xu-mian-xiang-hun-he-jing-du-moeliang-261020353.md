---
title: 'Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization'
title_zh: 超越专家排序：面向混合精度MoE量化的对比度校准框架NatScale
authors:
- Renjie Xie
- Juncheng Yang
- Aoting Hu
- Yan Liang
- Mingxi Zhang
- Zheheng Hong
- Wei Xu
- Yanzhi Chen
affiliations:
- Nanjing University of Posts and Telecommunications
- Tylogi AI Lab
- Anhui University of Technology
- Shanghai Jiao Tong University
- Southeast University
arxiv_id: '2610.20353'
url: https://arxiv.org/abs/2610.20353
pdf_url: https://arxiv.org/pdf/2610.20353
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: MoE混合精度量化 · 位宽分配优化
tags:
- MoE
- Quantization
- Mixed-Precision
- Contrast-Calibration
- Post-Training-Compression
one_liner: 提出基于对比度校准的NatScale框架，优化MoE混合精度量化的位宽分配效果
practical_value: '- 业务中部署MoE大模型做量化降本时，不要仅依赖专家重要性排序分配位宽，可复用对比度校准思路：以和均匀分布的对称KL散度为目标校准梯度权重的相对差异，在固定存储预算下提升量化后模型和原生模型的输出一致性

  - 评估专家量化误差时，要联合计算gate/up/down三个投影的输出误差，不要单独评估各模块误差，能更准确反映量化对最终输出的影响，该trick可直接嵌入现有量化pipeline

  - 若业务场景优先保障量化后模型和原生模型的输出对齐（比如Agent调用大模型、推荐场景的生成式内容生成），优先选择NatScale的分配策略，比现有基于路由频率、权重谱的方案保真度更高'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
MoE大模型通过稀疏路由降低单token计算量，但全量专家参数存储成本极高，混合精度量化是核心降本方案。现有方法仅基于梯度、路由频率等信号对专家做重要性排序分配位宽，未考虑专家权重误差的相对对比度，无法精准调控专家间的存储资源竞争强度，易出现重要专家位宽不足、冗余专家位宽浪费的问题。
### 方法关键点
- 对比度校准：对梯度计算得到的专家敏感度做保序幂变换，以权重分布和均匀分布的对称KL散度（默认1 nat）为校准目标，在不改变专家排序的前提下，精准调节权重的相对差异，控制专家间的存储竞争强度
- 联合误差估计：同时量化单个专家的gate、up、down三个投影模块，在固定原生输入下计算联合输出误差，避免单独评估各模块误差忽略交互影响的问题
- 全局最优分配：融合权重谱、方差、精度衰减的结构先验，生成每个专家配置的综合代价，通过LP松弛+可行舍入求解全局存储预算约束下的最优位宽分配
### 关键实验
在Qwen3.6-35B-A3B、Qwen3.8-Flash-Next、DeepSeek-V4-Flash-0731三个主流MoE模型，2.0/2.5/3.0 bpw三个存储预算下，和MxMoE、AlphaQ等5个SOTA基线对比，NatScale在全部9个场景下取得最低原生-量化KL散度、最高Top1 token一致性，7个场景下取得最低PPL；下游任务上Qwen3.8-Flash-Next在AIME、GPQA、TruthfulQA上均取得最优表现。
### 核心结论
MoE混合精度量化的效果不止取决于专家重要性排序，专家敏感度的相对对比度对存储分配的合理性影响更大。
