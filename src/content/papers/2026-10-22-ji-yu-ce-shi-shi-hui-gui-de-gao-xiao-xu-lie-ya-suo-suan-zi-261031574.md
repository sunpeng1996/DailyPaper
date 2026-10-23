---
title: Rethinking Sequence Compression with Test-time Regression
title_zh: 基于测试时回归的高效序列压缩算子TTR-Compressor
authors:
- Sihan Yang
- Jie Huang
- Hanxuan Li
- Yifan Guo
- Weigao Sun
- Yiran Zhong
- Weiyang Liu
affiliations:
- The Chinese University of Hong Kong
- Independent Researcher
- Token Foundry, Alibaba Group
- SphereLab
arxiv_id: '2610.31574'
url: https://arxiv.org/abs/2610.31574
pdf_url: https://arxiv.org/pdf/2610.31574
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: 大模型高效推理 · 序列压缩
tags:
- Sequence Compression
- Test-Time Regression
- Long Context LLM
- Multimodal LLM
- Token Merging
one_liner: 提出基于测试时回归的轻量序列压缩算子，在长上下文检索、多模态token合并任务上显著优于传统方案
practical_value: '- 长上下文用户行为序列建模场景，可直接将TTR-Compressor作为drop-in替换现有mean/attention pooling，仅新增2d参数即可提升长序列核心特征保留率，优化召回/排序效果

  - 多模态电商搜推广场景（商品图文/短视频特征压缩）可复用TTR的token合并逻辑，3×3压缩比下比传统MLP merger高2.58个指标点，同时减少55.6%视觉token降低推理成本

  - 电商Agent超长会话上下文压缩场景，可借鉴其二阶相关性建模思路，自动过滤冗余会话信息，提升长上下文理解准确率，同时降低KV cache占用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主流序列压缩方案（均值pooling、固定投影、attention加权pooling）仅建模token一阶统计特征，忽略token间二阶语义相关性，冗余信息易稀释核心特征，是长上下文LLM、多模态大模型的关键性能瓶颈，且普遍存在参数效率低、压缩效果差的问题。
### 方法关键点
- 重构序列压缩为测试时岭回归问题：每个输入序列单独构造回归任务，拟合得到的系数直接作为压缩表征；端到端训练时回归目标投影、正则化矩阵通过下游任务梯度更新，推理时用闭式解快速计算结果
- 双层优化设计：外层循环学习适配任务的回归目标与正则化参数，内层通过T×T Cholesky分解求解闭式解，复杂度仅O(T²d)，单压缩器仅含2d可训练参数，远低于传统投影方案的O(Td²)复杂度
- 引入token归一化+可学习对角正则化：归一化保证Gram矩阵仅建模语义相似度，可学习对角正则化无需手动调参，自动对不同特征维度施加差异化惩罚，强化冗余信息过滤能力
### 关键实验结果
- 块级稀疏注意力任务：在RULER长上下文检索数据集上，比最优基线（attention加权pooling）平均提升12.24个点，8K上下文单针检索准确率接近100%，32K长上下文泛化效果远超基线
- 多模态视觉token合并任务：2×2压缩比下比主流MLP merger平均高1.1个点，3×3压缩比下高2.58个点；3×3压缩的TTR效果接近2×2压缩的MLP，仅需44.4%的视觉token量
### 核心结论
序列压缩无需做静态加权聚合，可作为输入自适应的推理问题，通过建模token间二阶相关性高效过滤冗余信息，同时最大化保留核心特征。
