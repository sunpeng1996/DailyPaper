---
title: Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their
  Steps More, Independent of Post-Training
title_zh: 思维链依赖是否遵循缩放定律：大模型更依赖步骤且与后训练无关
authors:
- Esther Xin
affiliations:
- Independent Researcher
arxiv_id: '2610.38433'
url: https://arxiv.org/abs/2610.38433
pdf_url: https://arxiv.org/pdf/2610.38433
published: '2026-10-28'
collected: '2026-10-30'
category: LLM
direction: 大语言模型 · 思维链缩放规律
tags:
- Chain-of-Thought
- Scaling Law
- LLM Reasoning
- Faithfulness
- Model Evaluation
one_liner: 通过精确可控的盒子交换任务验证CoT依赖随模型规模上升饱和，核心驱动为能力而非后训练
practical_value: '- 做电商导购、订单查询类多步Agent任务时，优先选择≥1B参数的模型，可保证CoT步骤的负载性，避免中间推理沦为无效表面叙事，降低幻觉率

  - 小模型（<1B）无需投入成本做CoT相关SFT优化，其对CoT的天然依赖度极低，直接优化端到端任务能力性价比更高

  - 可借鉴论文的步骤编辑干预法，校验LLM+RAG推荐/导购链路是否真的依赖召回的外部信息与中间推理步骤，快速定位推理链路的幻觉风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
CoT是当前LLM推理、Agent多步决策的核心技术，也被视作LLM安全监测的重要抓手，但过往研究对「模型最终答案是否真的依赖CoT步骤」的度量缺乏精确的中间状态真值对照，不同研究关于模型规模、后训练对CoT依赖度的影响结论完全相反，急需可控实验验证规律。
### 方法关键点
- 设计完全可控的合成盒子交换任务，每个中间状态都有确定真值，通过编辑某一步的状态观测后续推理和答案是否跟随修改，精确量化CoT依赖度
- 覆盖25个开源模型（Qwen3、Gemma3、Llama3、OLMo2全系列，参数0.6B~14B，含base和后训练版本），单16GB T4即可跑完全量7200条/模型的推理实验
- 控制变量验证模型规模、推理能力、后训练、训练token数对CoT依赖的独立影响
### 关键结果
- CoT依赖度随模型规模上升并饱和：Qwen3系列0.6B时依赖度仅16%~18%，14B时达97%~100%，拟合logN的饱和逻辑曲线R²=0.89，拐点约1B参数
- 模型能力是核心驱动：25个模型的CoT依赖度和步骤准确率相关系数r=0.99，同等能力的不同架构/规模模型依赖度接近
- 后训练无额外影响：4B以上参数的base和后训练模型CoT依赖度差≤0.03，后训练仅通过提升能力间接影响依赖度
- 14B以下所有模型无法在无CoT的情况下完成≥4次交换任务，直接回答准确率接近随机的1/24

最值得记住的结论：对于超出模型内部推理容量的多步任务，模型规模越大，CoT的负载性越强而非越弱，直接支持CoT监测在复杂推理场景的有效性。
