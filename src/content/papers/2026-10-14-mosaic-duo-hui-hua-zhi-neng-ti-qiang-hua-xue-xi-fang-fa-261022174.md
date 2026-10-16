---
title: 'Mosaic: Multi-Session Agentic Reinforcement Learning'
title_zh: Mosaic：多会话智能体强化学习方法
authors:
- Yilong Xu
- Minrui Xu
- Xinyu Zhou
- Xiang Long
- Haochen Tan
- Zhijiang Guo
affiliations:
- LARK, HKUST(GZ)
- Foundation Model Lab, Huawei
- City University of Hong Kong
- HKUST
arxiv_id: '2610.22174'
url: https://arxiv.org/abs/2610.22174
pdf_url: https://arxiv.org/pdf/2610.22174
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 多会话Agent 强化学习优化
tags:
- Agentic RL
- Multi-session
- GRPO
- LLM Agent
- Reinforcement Learning
one_liner: 提出无critic分层优化的多会话Agent RL方法，解决训练推理会话假设不匹配问题，性能优于广播基线
practical_value: '- 电商导购/搜索Agent多会话训练可复用分层优势估计逻辑，为成功路径的少会话样本加权，降低推理会话开销

  - 多任务Agent的细粒度奖励设计可借鉴按会话类型归一化的trick，避免不同会话类型的奖励分布差异导致训练不稳定

  - 多轮搜索推荐全链路RL优化可复用边际信息增益的细粒度奖励塑造方法，无需额外训练critic，降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agentic RL默认单会话轨迹假设，但实际推理中上下文压缩、子Agent分叉等操作会生成跨多会话的轨迹，导致训练和推理假设不匹配；现有广播法直接将整条轨迹的优势复制给所有会话，无法区分不同会话的贡献，也无法引导会话合理分配，训练信号粗糙，优化效率低。
### 方法关键点
- 会话感知的轨迹级优势估计：将同任务分组的轨迹按成败分为子组，在子组内按会话数量做中心化排序，用有界调制因子修正GRPO的轨迹优势，保证成功轨迹中少会话样本优势更高，失败轨迹中多会话样本惩罚更低，且不会反转成败样本的优势符号
- 会话级优势塑造：将每个会话视为状态转移，计算会话前后模型生成正确答案的对数似然差作为边际信息增益，按会话类型分组归一化后与轨迹级优势融合，为不同会话分配差异化学习信号
- 整体为无critic的分层优化架构，无需额外训练价值网络，训练开销低
### 关键实验
在BrowseComp长路径搜索基准上，以Qwen3.5-4B为基座，对比单会话GRPO、IGPO、多会话广播法等基线：上下文压缩场景下，Mosaic较广播法准确率相对提升10.1%，平均每轨迹会话数从3.17降至2.35；子Agent分叉场景下准确率同样优于广播基线，会话数从4.43降至3.77。
### 核心结论
多会话Agent优化的核心不是增加会话数量，而是提升每个会话的效用，将计算资源分配到边际收益最高的执行阶段
