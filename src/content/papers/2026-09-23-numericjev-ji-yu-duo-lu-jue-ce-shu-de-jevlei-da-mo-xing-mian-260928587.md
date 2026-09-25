---
title: 'NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees'
title_zh: NumericJev：基于多路决策树的Jev类大模型免训练数值解码方法
authors:
- Weiwei Ye
- Hangchen Liu
- Renhe Jiang
affiliations:
- The University of Tokyo
arxiv_id: '2609.28587'
url: https://arxiv.org/abs/2609.28587
pdf_url: https://arxiv.org/pdf/2609.28587
published: '2026-09-23'
collected: '2026-09-25'
category: LLM
direction: LLM数值解码 · 免训练结构化推理
tags:
- Numerical Decoding
- Multiway Decision Tree
- Training-free
- LLM Inference
- Structured Output
one_liner: 免训练多路决策树递归缩小区间，让仅支持结构化选择的Jev类LLM输出高精度数值
practical_value: '- 电商/推荐场景做数值类预测（如用户下单概率、GMV预估、价格敏感度分档）时，无需微调LLM，仅通过多路区间选择调用结构化输出LLM接口即可获取稳定数值结果，省掉LoRA微调的标注数据和算力成本

  - 做Agent/生成式推荐的数值输出模块时，避免让LLM直接生成数字或做进制转换，采用区间选择的prompt范式可大幅降低数值错误，实验中相比直接候选选择的NMAE下降超64%

  - 线上低延迟场景可通过调整分支因子K平衡调用次数和精度，如K=10时输出100档精度数值仅需2轮调用，延迟可控，适配推荐/广告的实时推理需求'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Jev类仅支持结构化选择输出的LLM无法直接生成指定精度的数值；现有数值输出方案要么需要额外训练回归头，泛化性差且易丢失问题上下文，要么要求LLM做进制转换，错误率极高，免训练、保语义的高精度数值解码方案存在明确缺口。
### 方法关键点
- 完全免训练：无需修改LLM参数，也不需要访问模型隐状态，仅依赖LLM原生的结构化选择接口即可实现
- 多路决策树区间递归：每轮将当前数值范围划分为K个子区间，让LLM选择目标值所在区间，递归缩小范围直到达到指定精度，全程保留原始问题上下文
- 鲁棒性设计：采用整数索引计算避免浮点边界歧义，支持任意网格大小，无需网格为K的幂次
### 关键实验结果
- 数据集：256个覆盖加减乘除的算术表达式、3个标普500历史收盘价召回任务
- 对比基线：直接选择100个候选数值、LoRA微调的4B/9B大模型连续输出头、十进制/二进制编码输出
- 核心数字：K=10的NumericJev在算术任务上范围归一化MAE为1.84%，较直接候选选择的5.18%下降64.5%；5%相对误差内的样本占比83.4%，较直接选择高2.93个百分点；历史收盘价召回平均相对误差4.58%，提供正确值时读错率为0
### 核心结论
数值输出的分辨率和实际精度是完全独立的两个属性，看起来小数点后位数越多不代表结果越准确，早期区间选择错误会导致后续精度再高也无法挽回。
