---
title: Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation
  Steering
title_zh: 基于激活引导的细粒度推理控制 破解大模型推理自循环问题
authors:
- Sheldon Yu
- Tong Yu
- Xunyi Jiang
- Rohan Surana
- Gagan Mundada
- Sungchul Kim
- Lina Yao
- Julian McAuley
- Junda Wu
affiliations:
- UC San Diego
- Adobe Research
- University of New South Wales
arxiv_id: '2607.18100'
url: https://arxiv.org/abs/2607.18100
pdf_url: https://arxiv.org/pdf/2607.18100
published: '2026-07-20'
collected: '2026-07-21'
category: Reasoning
direction: 大模型推理控制 · 激活干预
tags:
- Activation Steering
- Reasoning Control
- Self-loop Mitigation
- Inference Intervention
- Steering Vector
one_liner: 无训练推理控制框架SOPHIA，通过隐状态激活干预在线破解LLM推理自循环，提升效率与准确率
practical_value: '- Agent做复杂任务（电商用户意图理解、多步导购决策）时，可复用自循环检测逻辑：对推理步骤做隐状态聚类，连续两步落在同一聚类就触发干预，避免token浪费、降低推理延迟

  - 激活干预的工程实现可复用：针对特定状态对预计算对比steering vector，推理时在线匹配当前状态直接调用，无需重训模型，适合生产环境快速落地

  - LLM做生成式推荐的CoT推理（如解释推荐理由、定制优惠文案）时，可参考聚类分层逻辑，识别冗余验证状态，跳过无效生成，提升文案生成效率与相关性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前大模型基于Chain-of-Thought的长推理链路极易陷入自循环，反复执行冗余验证、重复计算，不仅大量消耗token预算、提升推理延迟，统计结果显示这类过长的无效推理还和最终结果错误高度相关。现有推理控制方法多为prompt级调整或全局steering vector干预，无法针对推理过程的细粒度状态做精准匹配，难以有效破解自循环问题。
### 方法关键点
- 离线阶段：收集目标模型的推理轨迹，分割为步骤级单元，对步骤的最后一层隐状态做均值池化后用K-means聚类为5类隐推理状态，统计状态转移规律；对每个状态预计算对比steering vector，即跨状态转移样本的残差激活均值减去自循环样本的残差激活均值
- 在线阶段：采用双模型并行架构，嵌入模型实时对当前推理步骤做状态分类，检测到连续两步属于同一状态即判定为自循环，对目标推理模型的中高层残差流注入对应steering vector，引导模型跳出循环
- 全程无需微调模型权重，仅在推理时做轻量干预，支持跨模型大小、架构快速适配
### 关键结果
在GSM8K、AQuA、LogiQA、MATH 4个主流推理数据集上验证，对比无干预Greedy解码、随机向量扰动、反向steering 3个baseline，SOPHIA的自循环破环率平均提升30+百分点，部分难破环状态的hit rate从25%提升至100%，同时提升推理准确率、降低无效token消耗。
### 核心结论
LLM的推理过程存在可观测的隐状态转移规律，针对特定状态而非全局做激活干预，是低成本实现推理细粒度控制的可行路径
