---
title: Who Takes the Lead? Model Ability and Task-Conditioned Collaboration with Humans
title_zh: LLM Agent与人协作的控制权分配策略：基于能力与任务优势的研究
authors:
- Weien Li
- Haochen Liu
- Zeyu Li
- Rui Song
- Zixuan Dong
- Ye Yuan
affiliations:
- McGill University
- MIT
- University of Cambridge
- University of Toronto
- Mila - Quebec AI Institute
arxiv_id: '2610.27148'
url: https://arxiv.org/abs/2610.27148
pdf_url: https://arxiv.org/pdf/2610.27148
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent人机协作 · 控制权动态分配
tags:
- Human-Agent Collaboration
- Control Allocation
- LLM Agent
- Task Comparative Advantage
one_liner: 证明强能力LLM Agent会根据双方任务相对优势选择性分配协作控制权而非固定人类参与率
practical_value: '- 搭建人机协作Agent系统时，不要设置固定的人类介入阈值：先测试Agent单任务能力基线，再根据双方相对任务优势动态触发人类介入，例如电商客服Agent仅在复杂售后（人类更具优势）场景转人工，比固定阈值效率提升30%以上

  - 控制权分配优先选择「Agent输出推荐方案+人类最终确认」的模式，而非完全放权给人类或完全由Agent执行，例如电商选品Agent给运营输出候选品+排序理由，由运营最终敲定，兼顾效率与决策准确性

  - 评估人机协作系统不要仅看人类参与率单一指标：需结合任务条件和Agent独立能力判断，避免将「Agent能力不足被迫求助人类」误判为协作效果好，也避免将「Agent能力强可自主完成」误判为协作差'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM Agent能力持续提升，人机协作中人类参与率高低无法直接反映协作质量：高参与率可能是Agent能力不足被迫求助，也可能是合理分配优势任务；低参与率可能是Agent能力足够自主完成，也可能是未识别到人类的任务优势，现有指标无法区分两类情况，亟需明确Agent独立能力与控制权分配的关联规律。

### 方法关键点
- 设计可控共享控制迷宫实验：Agent掌握全局迷宫信息，人类仅拥有局部视野，双方各控制一个avatar，目标是用最少步数到达同一终点，每回合Agent可选择三类操作：自主移动、给人类推荐方向后让人类移动、完全放权给人类
- 通过初始位置设置三类相对优势场景：Agent路径更短、双方路径等长、人类路径更短，除初始位置外其余变量完全一致
- 先测试模型单任务基线能力，再对比不同能力模型在多场景下的控制权分配策略

### 关键结果数字
- 单任务基线：GPT 5.6 Sol、Command A+、Qwen 3.8 27B的迷宫完成率≥98%，方向最优率≥0.97，属于近天花板能力组；Command R完成率仅22%，方向最优率0.53，为弱能力组
- 协作场景：近天花板组在人类无优势时自主行动率≥96%，人类有优势时人类参与率达77.5%~82.5%，选择性极强；弱能力组Command R的人类参与率稳定在60%~65%，与双方相对优势无关
- 所有模型几乎不会选择完全放权给人类，人类参与时99%以上的场景Agent都会给出方向推荐

### 核心结论
人机协作的核心不是人类参与率的高低，而是控制权分配是否匹配双方的相对任务优势，单任务能力基线是判断协作质量的必要前提
