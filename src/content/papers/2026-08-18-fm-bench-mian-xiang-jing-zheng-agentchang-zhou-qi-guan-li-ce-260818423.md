---
title: 'FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents'
title_zh: FM-Bench：面向竞争Agent长周期管理决策的基准测试框架
authors:
- Tianyou Wang
- Chongyang Gao
- Kezhen Chen
- Chen Dong
- Yinghao He
- Donghan Li
- Wangcheng Xu
- Hongjiu Zhang
- Chi Li
affiliations:
- AnalogyAI
arxiv_id: '2608.18423'
url: https://arxiv.org/abs/2608.18423
pdf_url: https://arxiv.org/pdf/2608.18423
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: Agent 长周期决策能力评测
tags:
- LLM Agent
- Benchmark
- Long-Horizon Decision
- Multi-Agent Competition
- Tool Calling
one_liner: 首个融合长周期累积决策与多Agent竞争的LLM管理决策能力评测基准，支持双赛道评估与行为拆解
practical_value: '- 长周期决策类Agent（电商大促策略优化、商家运营Agent）可借鉴其能力拆解框架，从终局意识、资源利用率、主动规划、记忆管理4个维度优化行为，避免短视决策

  - 多Agent竞争场景（广告竞价、供应链博弈）可复用其确定性打分机制，规避LLM judge或人工评估偏差，同时区分静态/动态竞争环境下的Agent能力差异

  - 长周期Agent的记忆设计可参考仅保留自写notebook作为跨步状态的方案，强制Agent做记忆精简，避免冗余历史拖累决策，同时便于回溯决策原因

  - Agent选型无需迷信模型规模、价格，实测长周期决策表现才是核心指标，token消耗与长周期决策效果无显著相关性，可优先优化决策效率而非盲目堆token'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent评测多聚焦短周期、静态环境任务，缺失同时覆盖长周期累积决策、多Agent竞争、隐藏信息、多目标约束这四类真实管理场景核心需求的基准，无法有效衡量Agent的长期经营决策能力。

### 方法关键点
- 构建20个游戏年的足球俱乐部经营环境，包含26个工具接口，约340~400个决策节点，Agent仅可通过自写notebook传递跨节点状态，无历史对话上下文
- 设计双评测赛道：solo赛道中Agent与固定脚本对手对抗，Arena赛道15个主流LLM Agent与1个脚本锚点在同一共享世界竞争
- 确定性评分机制，无LLM judge或人工打分，得分由荣誉、净资产、阵容价值三个维度累积计算，同时拆解出终局意识、资源分配、主动控制、价格发现、记忆管理、计算效率6类行为能力

### 关键结果
15个主流LLM均完成全周期任务，而盲写脚本基线7/9的任务失败；claude-fable-5在solo赛道得分90.94，达到读取隐藏状态的oracle基线的95%；模型规模、价格、token消耗与最终得分无显著相关性，solo赛道第5年的排名与最终排名相关性仅0.19，第15年才提升到0.78；Arena赛道冠军在10个模型中轮换，无模型能持续统治，共享竞争环境下的表现与solo赛道表现差异显著。

> 长周期决策能力的核心是行为策略合理性而非计算资源投入，静态环境优势在动态竞争场景中会完全失效
