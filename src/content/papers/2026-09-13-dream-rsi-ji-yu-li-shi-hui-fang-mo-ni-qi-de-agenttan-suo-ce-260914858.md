---
title: 'Dream-RSI: Recursive Self-Improvement through Evolving Worlds'
title_zh: Dream-RSI：基于历史回放模拟器的Agent探索策略递归自改进框架
authors:
- Tong Zheng
- Xidong Wu
- Zheng Zhang
- Zhankui He
- Chaoyi Zhang
- Benjamin Coleman
- Ruoqiao Wei
- Di Bai
- Haolin Liu
- Rui Liu
affiliations:
- Google
- University of Maryland, College Park
- Google Deepmind
- University of Virginia
arxiv_id: '2609.14858'
url: https://arxiv.org/abs/2609.14858
pdf_url: https://arxiv.org/pdf/2609.14858
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 探索策略递归自优化
tags:
- Recursive Self-Improvement
- Exploration Policy
- Replay Simulator
- LLM Agent
- Dreaming
one_liner: 将历史发现树转化为回放模拟器，低成本离线迭代优化Agent探索策略，无需修改底层模型
practical_value: '- 电商/推荐场景的召回/排序探索策略优化，可将历史曝光点击日志结构化构造成回放模拟器，离线快速测评不同策略，无需上线AB测浪费流量，大幅降低策略迭代成本

  - 业务侧LLM Agent可将探索策略封装为独立可编程编排层，和底层推理/生成模型解耦，迭代策略时无需微调模型，仅调整编排逻辑即可，适配业务快速迭代需求

  - 新品冷启、新流量池探索等长周期场景，不要强行给Agent注入先验语义引导，易过度限制探索空间，用历史回放迭代策略的效果更优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent递归自改进的核心瓶颈是探索策略优化成本极高：固定探索策略无法适配复杂大搜索空间，在线优化探索策略需要长周期rollout，反馈延迟高、资源消耗大，现有方法仅将历史探索记录作为静态上下文或微调数据，未充分利用其结构化信息。

### 方法关键点
- 新增轻量可编程探索策略编排层，与底层编码Agent完全解耦，迭代策略时仅修改编排代码，无需改动基础模型
- 将在线探索生成的结构化发现树转换为回放模拟器，存储所有历史尝试的执行结果、得分、上下文信息
- 离线阶段通过「做梦」机制，在回放模拟器上快速测评数千种候选探索策略，无需重新执行Agent调用，零额外执行成本
- 按「探索质量-执行成本-并行效率」多目标打分筛选最优策略，重新部署到在线环节，形成自改进闭环

### 关键实验
跨算法工程、数学优化、GPU内核工程3个领域共8个任务，对比基线包括sklearn、glmnet、SimpleTES等SOTA系统。核心结果：算法工程任务相比固定探索基线减少1.7× Agent调用，比SimpleTES少162×调用；数学优化任务1k代内达到SOTA水平，比SimpleTES节省50×预算；GPU内核任务相同性能下少1.79~2.43×迭代次数，相同预算下性能提升1.44~2.09×。

### 核心结论
不要把历史探索记录仅当静态上下文，结构化的历史就是零成本的策略迭代模拟器，能把元优化的代价从在线量级降到离线仿真量级。
