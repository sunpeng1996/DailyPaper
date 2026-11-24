---
title: How Complete Must an Environment Be to Train a Capable GUI Agent?
title_zh: 训练高性能GUI Agent所需环境的完备性维度与优化方案
authors:
- Jingxing Wang
- Teng Wang
- Xingyu Lou
- Zihan Guo
- Jun Wang
- Weiwen Liu
- Weinan Zhang
- Jianghao Lin
affiliations:
- Shanghai Jiao Tong University
- OPPO Research Institute
- Shanghai Innovation Institute
arxiv_id: '2611.23946'
url: https://arxiv.org/abs/2611.23946
pdf_url: https://arxiv.org/pdf/2611.23946
published: '2026-11-17'
collected: '2026-11-24'
category: Agent
direction: GUI Agent 训练环境构建优化
tags:
- GUI Agent
- Environment Construction
- Reinforcement Learning
- Policy Optimization
- Mobile Agent
one_liner: 提出GUI训练环境完备性三维度框架，构建低成本高性能的MobileGym-Lite训练环境
practical_value: '- 训练交互类Agent（如电商导购Agent、APP操作Agent）时，reward设计必须覆盖所有可达成目标的路径，仅奖励单条参考路径会导致成功率下降10%以上，避免错误惩罚有效探索路径

  - 构建训练环境时可放心裁剪任务无关的功能模块，不仅能降低14%的代码量、33%的构建成本，还能避免长路径绕路的成功样本干扰多任务训练，提升下游任务泛化性

  - 多任务RL训练时可加入episode长度平衡机制，或后期收窄GSPO重要性裁剪阈值，避免长路径样本权重过高侵蚀已学会的短路径任务能力

  - 不要为降低成本删减任务无关的训练数据（如电商环境中非当前任务的商品、历史订单），否则会导致部署后在真实全量数据环境下成功率下降2~4个点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GUI Agent是交互类Agent的核心落地方向，但可执行训练环境构建成本极高，现有工作多凭工程经验裁剪环境，没有量化不同维度裁剪对Agent最终性能的影响，无法在成本和性能之间做最优权衡。

### 方法关键点
- 首次提出GUI环境完备性三维度框架：reward coverage（奖励覆盖的有效路径数）、data coverage（环境中任务无关数据的丰富度）、feature coverage（环境中任务无关功能的丰富度）
- 基于MobileGym平台控制单一变量，分别裁剪三个维度的完备性，训练Qwen3-VL-4B-Instruct模型，所有策略统一在全量环境下评估效果
- 引入episode长度加权对比实验，定位功能裁剪提升性能的核心机制：未裁剪环境中长路径绕路的成功样本权重更高，会干扰多任务模型的已有能力

### 关键实验
基于192个训练模板、155个评估模板共465个实例验证：全量环境基线成功率为51.61%；仅奖励单条参考路径时成功率降10.53个点；裁剪任务无关数据时成功率降1.93~4.30个点；裁剪任务无关功能时成功率升4.52个点至56.13%。基于结论构建的MobileGym-Lite裁剪了14%的代码量，在全量环境下成功率达55.48%，比基线高3.87个点。

**最值得记住的一句话**：GUI训练环境裁剪不需要追求全完备，奖励和数据维度要尽量保完备，功能维度可放心裁剪无关模块，反而能提升多任务训练性能。
