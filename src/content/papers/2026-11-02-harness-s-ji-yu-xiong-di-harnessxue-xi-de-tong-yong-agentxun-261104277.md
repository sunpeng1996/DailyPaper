---
title: 'Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training'
title_zh: Harness-S：基于兄弟Harness学习的通用Agent训练框架
authors:
- Kangning Zhang
- Wenxiang Jiao
- Bowen Fang
- Shuai Shao
- Jiachen Zhu
- Rong Shan
- Shijian Wang
- Hao Wang
- Yuan Lu
- Weiwen Liu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- Zhongguancun Institute of Artificial Intelligence
- Southeast University
- Carnegie Mellon University
arxiv_id: '2611.04277'
url: https://arxiv.org/abs/2611.04277
pdf_url: https://arxiv.org/pdf/2611.04277
published: '2026-11-02'
collected: '2026-11-06'
category: Agent
direction: Agent训练 · Harness优化与能力迁移
tags:
- Agent_Training
- Harness_Optimization
- GRPO
- Reinforcement_Learning
- Knowledge_Transfer
one_liner: 通过兄弟Harness池救助失败任务，将能力迁移到单一策略且在原Harness下保持有效
practical_value: '- 搭建电商领域Agent（客服、选品、工单处理等）时，可先针对基础prompt/流程的不同失败根因构建多套辅助Harness池，固定池避免反复迭代Harness的成本，提升训练效率

  - Agent RL训练遇到全失败无奖励信号的任务时，可借鉴救援机制：仅对全失败任务调用Top-K辅助Harness生成轨迹替换失败组，用GRPO更新共享策略，既补充有效训练信号又不会大幅增加采样成本

  - Harness路由可复用多LLM投票+行为画像动态刷新的设计，随策略迭代定期更新各Harness的适用场景画像，避免Harness效用随策略进化偏移导致的路由失效

  - 若需提升Agent在原始轻量Harness下的性能，可先通过功能更强的辅助Harness生成成功轨迹蒸馏到基础策略，无需在线部署复杂Harness，兼顾训练效果和推理效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent Harness优化存在两个核心痛点：一是局部修复的Harness难以合并为通用最优版本，易丢失各变体的差异化优势；二是Harness与策略联合迭代成本高，且优化后的收益往往无法迁移回原始基础Harness，导致推理时必须依赖复杂Harness部署，落地门槛高。

### 方法关键点
- **定向Harness演化**：从基础Harness出发，按不同失败根因生成专属兄弟Harness，选择覆盖互补失败场景的变体构建固定可复用的兄弟Harness池，训练阶段池保持不变，避免迭代开销
- **互补Harness救援训练**：仅当任务在基础Harness下所有采样轨迹全失败时，由自适应路由器选择Top-K辅助Harness，用相同策略生成新轨迹替换失败组，基于GRPO更新共享策略
- **自适应Harness路由器**：基于Harness行为画像（适用/规避场景）+多LLM投票选择匹配任务的Harness，随策略迭代定期刷新画像，适配Harness效用的非平稳性

### 关键实验
在AppWorld、SWE-Gym、DBBench三个长序列Agent基准测试，对比GRPO、Meta-Harness、WHALE等基线，Qwen3.5-4B版本在基础Harness下Pass@3比纯GRPO最高提升7.25pct，9B版本比GRPO提升7.63pct；搭配Rank-1路由后4B版本性能超过9B纯GRPO水平，且训练出的策略在未见过的外部Harness下仍有稳定增益。

最值得记住的一句话：不需要追求单个万能Harness，通过互补兄弟Harness的经验迁移，就能让基础Harness下的策略获得显著性能提升
