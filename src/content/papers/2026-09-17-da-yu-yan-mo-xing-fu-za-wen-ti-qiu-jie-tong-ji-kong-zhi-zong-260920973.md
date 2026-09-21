---
title: 'Complex Problem Solving in Large Language Models: A Statistical Control Survey
  and Diagnostic Framework'
title_zh: 大语言模型复杂问题求解：统计控制综述与诊断框架
authors:
- Jiazhang Cai
- Tao Wang
- Ruidong Zhang
- Siyuan Li
- Terry Ma
- Luyang Fang
- Haoran Lu
- Huimin Cheng
- Yingchuan Zhang
- Shushan Wu
affiliations:
- University of Georgia
- Carnegie Mellon University
- Harvard University
- Stanford University
- Icahn School of Medicine at Mount Sinai
arxiv_id: '2609.20973'
url: https://arxiv.org/abs/2609.20973
pdf_url: https://arxiv.org/pdf/2609.20973
published: '2026-09-17'
collected: '2026-09-21'
category: Reasoning
direction: LLM复杂推理 · 过程控制框架
tags:
- Complex Problem Solving
- Process Control
- Statistical Decision
- Uncertainty Quantification
- Error Diagnosis
one_liner: 将LLM复杂问题求解建模为隐状态序列估计决策问题，提出控制匹配的诊断优化框架
practical_value: '- 优化Agent任务执行链路：可参考论文的错误-干预匹配表，针对不同失败模式（如早期错误传播、多采样结果一致错误）选择对应干预措施，避免盲目增加思考步数或采样量浪费算力

  - 多步推荐场景适配：在大模型驱动的个性化消费规划、多跳关联商品推荐等长路径任务中，引入显式状态表示+步骤校验+回滚机制，降低早期错误放大导致的最终结果失效概率

  - 推理成本控制：参考误差三分法框架，将LLM推理错误拆分为系统偏差/随机方差/不可约噪声，针对不同错误类型分配计算资源：系统误差优先优化prompt或工具调用，随机误差才用多采样一致性，可大幅降低推理成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM复杂问题求解（CPS）研究普遍聚焦推理能力升级，但无法解释早期错误放大、prompt脆弱、错误承诺无法修正等典型失败模式，纯靠扩容模型、延长Chain-of-Thought长度往往无法解决问题甚至劣化效果，缺乏统一的过程控制框架定位失败根因、匹配优化手段。

### 方法关键点
- 将CPS建模为隐解空间的序列估计决策问题，明确区分「推理」（候选步生成）和「过程控制」（状态更新、动作决策）两大模块，控制动作包含提交、校验、分支、回滚、弃权五类
- 拆解控制框架为五大核心组件：显式状态表示、转移结构约束、校验与约束执行、搜索与回滚、不确定性管理，可覆盖CoT、ToT、ReAct、多智能体协作等现有主流方法的控制逻辑
- 提出误差三分法：系统偏差（多采样结果一致的共性错误）、随机方差（多采样结果波动的偶发错误）、不可约噪声，定义「问题-控制匹配」原则，针对不同失败特征匹配对应干预手段，避免控制错配

### 关键结果数字
- 自一致性策略在GSM8K数据集上将PaLM-540B准确率从56.5提升到74.4，但在CommonsenseQA上仅从79.0提升到80.7，符合方差优化仅对随机误差有效的结论
- GSM-HARD算术推理数据集上，程序辅助提示（PAL）相比普通CoT将Codex准确率从23.1提升到61.2，对应系统计算偏差用工具校验的优化效果

### 最值得记住的一句话
盲目增加推理步数或采样量无法解决所有CPS失败，针对错误根因匹配控制措施才能在固定计算预算下最大化收益
