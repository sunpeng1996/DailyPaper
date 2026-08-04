---
title: 'PredAct-Bench: Benchmarking Tool-Augmented Dialogue under Controlled Tool
  Noise'
title_zh: PredAct-Bench：可控工具噪声下工具增强对话评测基准
authors:
- Abdulrahman AlRabah
- Xiaocheng Yang
- Dilek Hakkani-Tür
- Abdussalam Alawini
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2608.02372'
url: https://arxiv.org/abs/2608.02372
pdf_url: https://arxiv.org/pdf/2608.02372
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent工具调用鲁棒性评测基准
tags:
- Agent
- Benchmark
- Tool-Use
- Trust-Calibration
- Noise-Robustness
one_liner: 首个可控工具噪声下工具增强对话基准，覆盖教育测试场景与多轮信任校准指标
practical_value: '- 工具增强Agent上线前可参考本文的可控噪声注入方法做鲁棒性测试，模拟真实场景下召回、预测工具的错误率波动，避免上线后过度信任错误输出导致业务损失

  - 可复用RAIR/RSR指标评估人-Agent协作场景的信任校准水平，比如电商运营助手、智能客服场景下，判断Agent是否能引导用户合理采纳建议而非盲目服从

  - 做多轮对话Agent设计时，可加入对话前后决策质量差值指标，提前识别多轮交互反而降低决策效果的问题，优化对话策略减少无效查询'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具增强对话与Agent基准普遍假设工具输出完全准确，忽略真实部署中工具存在随机误差、人对Agent信任度不确定的现实，高风险决策场景下（如电商风控、广告投放决策），Agent过度信任错误工具输出会造成严重业务损失。
### 方法关键点
- 以教育领域学生风险预警为测试场景，构建包含真实轨迹数据集OULAD、合成轨迹数据集PredAct-CS的评测基准，覆盖12种工具（含确定性查询、概率预测两类）
- 设计可控噪声注入机制，可将概率预测工具的准确率控制在40%~80%区间可调，仅修改预测结果保留置信度，模拟真实工具的置信度与准确率错配问题
- 提出多轮对话下的信任校准指标：RAIR（衡量决策者自身错误、Agent正确时采纳建议的比例）、RSR（衡量决策者自身正确、Agent错误时坚持判断的比例）
### 关键结果
评测13款SOTA闭源/开源LLM，搭配13名真人教师对照实验：
- 仅GPT-5.5、Gemini系列3款模型通过多轮对话提升决策F1，其余10款模型对话后F1平均下降7分，普遍存在过度信任工具输出问题
- 真人教师RAIR达0.63、RSR达0.88，处于校准最优区间，11款LLM的RAIR低于0.2，几乎不会修正自身初始错误
- 工具准确率从40%提升到80%时，LLM平均F1在PredAct-CS上从36升至73，工具可靠性对决策质量的影响与模型能力差距相当
### 核心结论
用完美工具评测得到的工具调用能力不具备真实部署价值，只有在可控噪声下仍能保持合理信任校准的Agent才能适配真实场景。
