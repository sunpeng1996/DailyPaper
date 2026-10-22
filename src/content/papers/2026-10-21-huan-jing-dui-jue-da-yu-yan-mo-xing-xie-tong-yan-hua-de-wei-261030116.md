---
title: 'Environment Duels: A Microcosm of LLM Co-Evolution'
title_zh: 环境对决：大语言模型协同演化的微观观测框架
authors:
- Shibo Jin
- Zhiqiu Xu
- Yiling Zou
- Shangyu Gong
- Mayur Naik
affiliations:
- University of Pennsylvania
arxiv_id: '2610.30116'
url: https://arxiv.org/abs/2610.30116
pdf_url: https://arxiv.org/pdf/2610.30116
published: '2026-10-21'
collected: '2026-10-22'
category: Eval
direction: Agent 动态评测 · LLM 协同演化
tags:
- AgentBenchmark
- LLMCoevolution
- SyntheticTrainingData
- ReinforcementLearning
- HintGuidedLearning
one_liner: 提出LLM同时作为环境作者与求解者的动态评测框架，揭示二者能力差异与协同演化规律
practical_value: '- 生成Agent训练用合成环境时，可复用「无hint通过率低、有hint通过率高」的校准指标筛选优质数据，大幅降低无效训练成本，尤其适合电商客服、导购Agent的场景化训练

  - 不用盲目选用最大基座生成训练数据，中小模型经过环境创作专项训练后，产出的训练环境质量可远超顶级大模型，兼顾效果与成本

  - 正式训练前可先测试目标模型对不同数据源的hint lift值，预判该数据源的训练收益，无需全量跑训练即可快速筛选最优训练集

  - 做业务系统效果评测时可复用「模型互相出题」的动态基准模式，无需人工标注即可自动提升评测集难度，解决传统基准快速饱和的问题'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前前沿LLM的训练高度依赖其他模型生成的合成数据与交互环境，传统固定基准易饱和，且无法量化LLM作为训练数据创作者的能力，也难以观测不同模型间的协同演化效应，亟需动态框架量化这类交互。

### 方法关键点
- 每个参与LLM同时扮演双角色：① 环境作者：生成交互式可执行环境+专属hint，目标设定为求解者无hint难通过、有hint易通过；② 环境求解者：分别在有/无hint条件下完成所有模型生成的环境任务
- 环境生产流程：Plan（设计规则与hint）→ Implement（写标准Python环境代码）→ Validate Review（沙箱验证+自审查，最多2次修复）→ Counter-move（查看求解轨迹后优化环境与hint）
- 核心指标：求解率（无hint下的任务通过率）、难度（所有求解者的无hint失败率）、hint lift（有hint相对无hint的通过率提升值）

### 关键结果
实验覆盖9个前沿LLM，共生成90个环境、12960次交互：① 小模型DeepSeek-V4.1-Flash、Gemini-3.8-Flash、Qwen3.8-27B的环境难度与hint lift远超最强求解者Claude-Opus-5、GPT-5.6-Sol；② hint lift与训练收益完全正相关：Qwen3.8-27B对GPT-5.6-Sol的环境hint lift为17.5，训练后平均得分提升2.0，对DeepSeek-V4.1-Flash的环境hint lift为5.0，训练后平均提升仅0.1。

**最值得记住的一句话**：LLM的解题能力和出题能力是完全独立的，经过专项训练的中小模型反而能产出质量更高的训练用合成环境，hint lift可提前预判训练收益。
