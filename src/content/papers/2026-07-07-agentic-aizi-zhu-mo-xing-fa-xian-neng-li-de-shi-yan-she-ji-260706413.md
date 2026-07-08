---
title: An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model
  Discovery
title_zh: Agentic AI自主模型发现能力的实验设计评估框架
authors:
- Hao He
- Xueying Liu
- Chris J. Kuhlman
- Xinwei Deng
affiliations:
- Virginia Tech
- Baylor University
arxiv_id: '2607.06413'
url: https://arxiv.org/abs/2607.06413
pdf_url: https://arxiv.org/pdf/2607.06413
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: Agent能力评估 · 多变量效用对齐分析
tags:
- Agentic AI
- Model Discovery
- Experimental Design
- Cost-aware Evaluation
- Multivariate Analysis
one_liner: 提出多维度实验设计框架量化Agent推理努力对模型质量、成本、复杂度的联合影响
practical_value: '- 评估LLM编码Agent完成推荐/广告场景的特征工程、模型迭代、用户行为模拟等任务时，可复用该多因子受控实验框架，量化推理努力、训练数据量等参数的投入产出比，避免无效资源浪费

  - 给Agent设定优化目标时需优先锚定核心业务指标，可参考文中的效用对齐计算方法权衡性能与成本，避免为非核心指标过度提升推理力度带来的不必要开销

  - 不要完全信任Agent对生成结果的自我评估，尤其在生成式推荐、用户行为模拟这类生成任务上，必须补充外部离线/在线校验流程，避免错误结果上线

  - 业务对成本敏感时，不要盲目提升Agent的推理努力档位，高推理档位仅提升代码复杂度和调用成本，对模型质量增益有限，可优先测试低档位的性价比'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM编码Agent已可自主完成数据建模、特征工程、模型迭代等工作，但现有评估多为单次基准测试，无法量化其随机性带来的结果波动，也无法明确推理努力、训练数据量等控制参数对模型质量、调用成本、运行效率的联合影响，无法为业务侧Agent配置提供可落地的量化指导。

### 方法关键点
- 将编码Agent视为随机模型发现算子，设计6因子全因子实验，分层控制Agent类型（Codex、Claude Code）、任务类型（用户行为预测/群体行为生成）、优化指标，可变因子包含3档推理努力、3折交叉验证、2种训练数据量档位，累计144组受控实验
- 采集8维度响应结果：核心/非核心指标性能、美元成本、运行时间、候选模型数、特征数、建模决策数、提交代码长度，做多维度联合分析
- 提出效用对齐正则分解（UACD）方法，计算推理努力的影响方向与预设的「性能提升、成本下降」效用方向的对齐度，量化投入产出效率

### 关键结果
数据集为28组网络组字谜游戏的用户行为序列，对比Codex和Claude Code两个商用Agent，核心结论：1）更高推理努力使两个Agent的token消耗提升2-3倍、代码长度提升1倍，仅在1/4任务上带来核心指标显著提升；2）7/8实验组的推理努力提升与预设效用方向负相关，即更高推理努力反而降低投入产出比；3）Agent对生成任务的自我评估准确率不足20%，对预测任务的自我评估准确率接近90%。

最值得记住的结论：推理努力本质是资源控制参数而非可靠的模型质量提升手段，盲目拉高推理档位只会显著提升成本，不会带来匹配的性能增益。
