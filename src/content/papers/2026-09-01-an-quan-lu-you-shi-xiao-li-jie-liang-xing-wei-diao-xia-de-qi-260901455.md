---
title: 'When Safety Routing Breaks: Understanding Alignment Fragility under Benign
  Fine-Tuning'
title_zh: 安全路由失效：理解良性微调下的LLM对齐脆弱性
authors:
- Yitong Guo
- Xiaoyi Chen
- Siyuan Zhang
- Xiaofeng Wang
- Haixu Tang
affiliations:
- Indiana University Bloomington
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2609.01455'
url: https://arxiv.org/abs/2609.01455
pdf_url: https://arxiv.org/pdf/2609.01455
published: '2026-09-01'
collected: '2026-09-02'
category: LLM
direction: LLM安全对齐 · 微调鲁棒性
tags:
- LLM Alignment
- Fine-tuning Robustness
- Fisher Geometry
- Safety Routing
- LoRA
one_liner: 从Fisher几何视角解释良性微调破坏LLM安全对齐的机理，验证低秩安全路由假说
practical_value: '- 业务侧小样本微调（如电商导购Agent、客服生成模型）优先选择LoRA而非全参数SFT，可在100样本级微调场景下将安全攻击成功率涨幅从85.7%降至24.5%，大幅降低合规风险

  - 若微调后模型安全能力退化，无需全量重对齐：仅需10~50条安全样本微调即可将ASR恢复至0，甚至推理时添加固定拒绝前缀就能降低50%以上ASR，修复成本极低

  - 垂直领域LLM对齐优化时，可重点监控最后几层MLP模块的参数变化，该区域是安全路由的核心控制点，能提前预警安全能力退化

  - 千级以上样本的大规模微调场景下，LoRA、ASAM的安全防护效果会失效，需提前补充推理侧安全拦截层作为兜底保障'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
对齐后的LLM在下游任务良性微调时，即使微调数据不含任何有害样本，也会大幅丧失有害请求拒绝能力，此前主流的梯度冲突解释无法覆盖随机样本也能触发安全崩溃的现象，亟需明确底层机理以指导实际微调的安全保障。
### 方法关键点
- 采用分块Fisher几何分析，逐层逐模块量化安全任务与通用任务的曲率变化，定位安全能力的参数分布区间
- 结合logit-lens与跨条件激活补丁实验，验证安全表征的留存性与最终层对拒答行为的因果控制作用
- 对比全参数SFT、LoRA、ASAM三类微调方案的安全退化规律，验证低秩安全路由假说
### 关键结果
实验覆盖Llama3.1-8B、Qwen2.5-7B两类主流开源模型，用Alpaca、Dolly作为良性微调数据集，HEx-PHI等作为安全评估基准：
- 仅100条随机良性样本即可让初始ASR=0的对齐模型ASR飙升至85.7%，而通用任务准确率仅下降10%左右，呈现不对称脆弱性
- 小数据量下LoRA可将ASR涨幅从85.7%降至24.5%，但微调样本量达5000时防护失效，ASR仍升至58.8%
- 仅需10条安全样本即可让微调后安全崩溃的模型ASR恢复至0，添加固定拒绝前缀可直接降低50%以上ASR
> 最值得记住的结论：LLM的安全对齐本质是低秩的输出侧路由机制，而非全局表征嵌入，因此极易被微调破坏但也极易修复
