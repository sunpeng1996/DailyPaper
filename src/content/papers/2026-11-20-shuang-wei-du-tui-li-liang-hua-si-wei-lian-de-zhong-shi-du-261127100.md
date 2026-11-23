---
title: 'Reasoning in Two Dimensions: Quantifying Chain-of-Thought Faithfulness and
  Efficiency'
title_zh: 双维度推理：量化思维链的忠实度与效率
authors:
- Chenruo Liu
- Quan Zhang
- Qi Lei
affiliations:
- New York University
- Michigan State University
arxiv_id: '2611.27100'
url: https://arxiv.org/abs/2611.27100
pdf_url: https://arxiv.org/pdf/2611.27100
published: '2026-11-20'
collected: '2026-11-23'
category: Reasoning
direction: CoT推理忠实度与效率量化优化
tags:
- Chain-of-Thought
- Faithfulness
- Reasoning Efficiency
- RFT
- Information Theory
one_liner: 提出信息论统一框架量化CoT忠实度与效率，配套低开销微调优化策略
practical_value: '- 业务侧使用CoT的Agent（比如电商客服、导购Agent）可复用该框架的双维度指标，不依赖人工标注就能识别高不确定性的推理路径，提前拦截错误回复，降低客诉风险

  - 做生成式推荐/搜索query多跳推理时，可直接复用效率感知RFT微调策略，剪去CoT中的off-path冗余步骤，推理token消耗降低最多20%，且不损失推理正确率，显著降本

  - 可借鉴语义推理图的思路，将用户多轮搜索/推荐交互的意图拆解为依赖图，识别无效推理分支，提升多轮意图理解的准确率和响应速度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有CoT评估仅以最终答案正确率为核心指标，既无法判断LLM是否真的依赖输出的推理步骤完成预测，也无法量化推理过程的冗余程度；同时忠实度和效率的度量长期割裂，缺乏统一框架，且直接优化相关指标的计算开销极高，难以落地到业务场景。
### 方法关键点
- 将CoT抽象为语义推理有向超图，把LLM的预测依赖拆解为「语义支持依赖/额外历史依赖」「答案相关推理/偏离路径推理」两个正交维度，基于信息论KL散度推导得到全局和步骤级的不忠实度、低效度量化指标
- 提出低开销的RFT微调策略：忠实度感知RFT通过加权语义图分布正则化降低非语义依赖；效率感知RFT直接剪去偏离路径的推理步骤后微调，两者可联合优化，无需直接计算高开销的度量指标
### 关键实验
在MATH、Omni-MATH-2、2WikiMultiHopQA三个数据集上测试Qwen3、Llama3、Ministral系列模型：① 指标响应符合预期：隐藏答案提示使答案不忠实度提升1.87~3.28×10⁻²，要求精简推理使低效度降低38.2%~68.7%；② 答案不忠实度与答案预测熵的Spearman相关系数达0.33~0.796，而忠实度、效率与答案正确率无稳定关联；③ 联合微调可同时降低不忠实度和低效度，Pass@1无损失甚至略有提升，推理token消耗最多下降19.7%
### 核心结论
CoT的正确率和简洁性无法完全反映推理质量，可靠的推理评估必须同时考虑预测依赖的忠实性和分配效率
