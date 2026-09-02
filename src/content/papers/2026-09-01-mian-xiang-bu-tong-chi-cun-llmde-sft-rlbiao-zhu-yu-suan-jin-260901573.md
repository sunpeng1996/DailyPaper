---
title: Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large
  LLMs
title_zh: 面向不同尺寸LLM的SFT-RL标注预算近似最优分配方法
authors:
- Jingtan Wang
- Arun Verma
- Xiaoqiang Lin
- Zhengyuan Liu
- Nancy F. Chen
- Daniela Rus
- Bryan Kian Hsiang Low
affiliations:
- National University of Singapore
- Singapore-MIT Alliance for Research and Technology
- Agency for Science, Technology and Research (A*STAR)
- Massachusetts Institute of Technology CSAIL
arxiv_id: '2609.01573'
url: https://arxiv.org/abs/2609.01573
pdf_url: https://arxiv.org/pdf/2609.01573
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: LLM后训练 · 标注预算分配优化
tags:
- SFT
- RLHF
- DPO
- GRPO
- Annotation Budget
- Transfer Learning
one_liner: 提出近优区域框架，通过小代理模型确定大模型SFT与RL阶段的标注预算分配比，避免大规模穷举搜索
practical_value: '- 业务场景微调LLM（如Agent工具调用、推荐文案生成对齐）时，无需精准穷举SFT/RL的预算比，取5%-10%性能容忍的近优区间即可，大幅降低调优成本

  - 做大模型对齐时，可先用同系列小参数量模型跑SFT/RL分配比的近优区间，直接迁移到大模型使用，无需在大模型上做全量网格搜索，节省算力和标注成本

  - 若SFT标注成本远高于RL（如电商场景高质量问答对成本远高于偏好标注），近优区间会更宽，可优先结合标注成本、样本复用等业务约束分配预算，无需过度纠结最优比'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM后训练流程通常采用SFT接RL的两阶段结构，但固定标注预算下如何在两个阶段分配资源缺乏可落地的指导框架：过往研究仅能观测到低数据量下SFT占优的粗略趋势，且最优分配比是否可跨模型尺寸迁移尚不明确，在大模型上穷举搜索最优分配比的时间、算力、标注成本极高，亟需低成本的通用分配方案。
### 方法关键点
- 放弃寻找单一最优分配比，定义**ε-近优区域**：性能不低于峰值性能(1-ε)的所有SFT预算占比的集合
- 提出跨尺寸迁移策略：在同系列小代理模型上确定近优区域，直接迁移到大目标模型使用，无需大模型端的全量搜索
- 覆盖DPO（off-policy RL）、GRPO（on-policy RL）两类主流RL对齐方法，同时适配SFT与RL标注成本不对称的业务场景
### 关键结果
- 实验覆盖数学、指令跟随、摘要、有用性4类任务，测试Llama 3、Qwen 2.5、Qwen 3三个模型家族（参数1B~14B），预算范围0~15k标注样本
- 仅需2%~10%的性能容忍，近优区域即可覆盖55%~75%的可行分配空间，且模型尺寸越大，近优区域越宽，分配灵活度越高
- 小模型近优区间迁移到大模型的准确率：ε=5%时达94.3%，ε=10%时达97.1%，适配DPO、GRPO两种RL方法及SFT/RL标注成本比1~10的所有测试场景

LLM后训练SFT与RL的预算分配不存在唯一最优解，只需在小模型上确定的近优区间内取值，即可在大模型上以极低的调优成本获得接近峰值的性能。
