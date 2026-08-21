---
title: 'Phantom Gains: Auditing Self-Improvement Against a Measured Null'
title_zh: 大语言模型自提升虚假增益审计：基于实测空值的校验框架
authors:
- Cheng Xu
- Nan Yan
- Liming Chen
- M-Tahar Kechadi
affiliations:
- University College Dublin
- Georgia Institute of Technology
- Dalian University of Technology
arxiv_id: '2608.20290'
url: https://arxiv.org/abs/2608.20290
pdf_url: https://arxiv.org/pdf/2608.20290
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: 大模型自提升评估 · 测量偏差校准
tags:
- LLM Self-Improvement
- Evaluation Bias
- LoRA
- Statistical Audit
- Null Testing
one_liner: 揭示7种LLM自提升评估的测量偏差，提出基于实测空值的无阈值校验方法
practical_value: '- 评估LLM驱动的推荐query理解、Agent工具调用效果时，禁止用单次greedy decode结果做对比，建议采样k≥128次计算pass@概率，规避batch推理随机波动带来的虚假效果差异

  - 做LoRA微调、prompt优化的AB实验时，必须加入frozen控制组跑完全相同的pipeline得到噪声基线，避免把采样误差误判为优化带来的真实增益

  - 对比不同微调/训练策略效果时，至少跑3个训练种子，避免单种子波动导致错误的方法选型结论

  - 统计方案是否解决了过往无法处理的case时，不要用固定阈值的能力扩张指标，改用基于多基线池的FDR控制精确检验，避免虚报效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM自提升评估已从单一准确率指标转向逐问题的能力变迁分析，判断模型新增/遗忘了哪些能力，但这类分析本质是两次带噪声的评估结果的差值，极易把采样误差当成真实的能力变化，现有方法普遍缺乏对测量噪声的校验，大量公开结论存在偏差。
### 方法关键点
- 引入**frozen控制组**：初始模型不做任何训练，跑完全相同的评估pipeline，为每个统计指标实测噪声基线，所有结论必须超过基线才成立
- 替换单次greedy decode为多采样solve rate估计：每个问题采样k=128次计算正确率，搭配带滞回的状态判定规则，过滤随机波动
- 提出无阈值的逐问题检验：把所有初始模型的独立评估结果汇总为公共基线池，在FDR控制下做Fisher精确检验，替代原有阈值式的扩张率（ER）指标
- 识别出7种常见的测量失败模式，每种都可通过低成本的方案校准，多数不需要新增实验
### 关键实验
基于Qwen3-8B的rank-32 LoRA训练，对比STaR、多数投票自训练、外部蒸馏三类方案，在MATH-500、AIME 2025/2026数据集上测试：
- 单次greedy decode会给无训练的frozen模型造出CLR=1.5的虚假遗忘/增益，2%的状态翻转完全来自推理噪声
- 原有ER1扩张率指标给frozen模型测出0.280的虚假扩张率，哪怕调为m=2的常用修复阈值，空值仍有0.058
- 校准后发现：外部蒸馏可提升8-11个基础模型极少答对的问题，3种自训练方法最多仅提升0-2个；且自训练会破坏88-106个基础模型已掌握的问题，远高于8的噪声基线
### 核心结论
任何能力变迁类的评估，所有统计指标都必须对应实测的噪声基线，而不能默认空值为0。
