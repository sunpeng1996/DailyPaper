---
title: 'Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon
  Terminal Tasks with Dense Reward-Based Grading'
title_zh: Long-Horizon-Terminal-Bench：长周期终端Agent任务的密集奖励评估基准
authors:
- Zongxia Li
- Zhongzhi Li
- Yucheng Shi
- Ruhan Wang
- Junyao Yang
- Zhichao Liu
- Xiyang Wu
- Anhao Li
- Yue Yu
- Ninghao Liu
affiliations:
- Tencent HY LLM Frontier
- University of Maryland, College Park
- University of Georgia
- University of Minnesota, Twin Cities
- Indiana University
arxiv_id: '2607.08964'
url: https://arxiv.org/abs/2607.08964
pdf_url: https://arxiv.org/pdf/2607.08964
published: '2026-07-08'
collected: '2026-07-13'
category: Agent
direction: Agent长程任务能力评估基准
tags:
- Agent Evaluation
- Long Horizon Task
- Dense Reward
- Terminal Agent
- Benchmark
one_liner: 构造46个长周期终端Agent任务集，用子任务级密集奖励替代二元判分，更准确评估长程执行能力
practical_value: '- 电商/广告场景下的长流程Agent（如全链路投放优化、多阶段用户运营）评估，可借鉴子任务拆解+密集奖励的设计，替代仅看最终转化的二元评估，精准定位Agent的能力瓶颈（如素材生成/出价策略/人群定向哪个环节出错）

  - 长程Agent训练中，可复用该分级打分逻辑设计过程奖励函数，给中间正确步骤即时反馈，大幅提升多阶段任务的训练收敛效率

  - 评估自研Agent长程能力时，可直接复用该基准的容器化执行框架与评分逻辑，无需从零搭建长任务评估体系，降低评估成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有终端Agent基准多聚焦短程任务，仅通过最终结果二元判分，奖励信号稀疏，既无法准确反映长周期（数十分钟至数小时、上百步操作）下Agent的规划、长上下文管理、迭代调试能力，也无法定位任务失败的具体环节，难以支撑长程Agent的迭代优化。
### 方法关键点
- 构建46个覆盖9个领域的长周期终端任务，包含实验复现、软件工程、多模态分析、科学计算等真实场景，每个任务平均需要200+轮交互、数十至上百次操作才能完成
- 设计子任务级密集奖励机制：将大任务拆解为多个语义独立的子任务，按权重累加得分，支持二元校验、连续阈值、跨轮次聚合三类子任务判分规则，可量化中间进度并给出部分得分
- 所有任务基于Docker容器化运行，设置低权重公开校验用例和高权重隐藏压力用例，避免Agent过拟合可见测试点
### 关键结果
测试15个前沿大模型，单任务平均消耗9.9M Token、执行85.3分钟、231轮交互；最强模型GPT-5.5在0.95奖励阈值下pass@1仅15.2%，1.0阈值下仅10.9%，所有模型平均pass@1分别为4.3%和1.7%；62.8%的运行获得部分奖励但未达及格线，二元判分会将其全部判定为失败，无法区分模型能力差异。
### 核心结论
当前Agent长周期任务的核心瓶颈不是局部推理正确性，而是长程预算管理、进度跟踪与自校验能力
