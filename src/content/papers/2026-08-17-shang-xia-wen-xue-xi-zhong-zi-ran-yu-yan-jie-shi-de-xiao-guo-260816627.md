---
title: When Do Explanations Help In-Context Learning? A Comparative Study of Natural
  Language Explanation Types and Faithfulness
title_zh: 上下文学习中自然语言解释的效果对比与忠实度影响研究
authors:
- Mahdi Dhaini
- Adam Dejl
- Juraj Vladika
- Volkan Özer
- Barbara Plank
- Gjergji Kasneci
affiliations:
- LMU Munich
- Imperial College London
- Technical University of Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2608.16627'
url: https://arxiv.org/abs/2608.16627
pdf_url: https://arxiv.org/pdf/2608.16627
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: 大模型上下文学习 · 解释增强Prompt优化
tags:
- In-Context Learning
- Natural Language Explanation
- Faithfulness
- Prompt Engineering
- Few-shot Learning
one_liner: 跨6类基准4种模型对比三类自然语言解释的ICL效用，明确忠实度筛选与语义对齐的影响规律
practical_value: '- 做Agent/LLM驱动的电商意图分类、推荐理由生成等任务时，优先选用外部LLM预生成NLE作为few-shot样例，效果与人类标注相当，成本降低1-2个数量级，无需额外忠实度筛选即可获得稳定收益

  - 若采用目标模型自生成NLE做few-shot，不要依赖单一忠实度度量做筛选，两类主流忠实度度量的标注分歧可达50%，需结合具体任务做AB测试，数学推理类任务忠实度筛选收益更显著

  - 做Prompt鲁棒性验证时，可加入同域NLE随机替换、跨域OOD NLE替换的压力测试，验证语义对齐的影响，避免工业场景中样例解释错配导致的效果下跌

  - 小参数SLM部署分类类任务（如商品类目预测、Query意图识别）时，添加NLE的few-shot增益比大模型更明显，可通过外部LLM预生成NLE库降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自然语言解释（NLE）被广泛用于增强In-Context Learning（ICL）的few-shot提示效果，但不同来源NLE的效用差异、忠实度筛选的实际影响、错配解释下的鲁棒性均缺乏系统验证，且三类NLE的获取成本差异极大，从业者缺少明确的选型指导。

### 方法关键点
- 覆盖三类NLE来源：人类标注NLE、目标模型自生成Ph-CoT解释、外部LLM生成解释
- 三种NLE筛选策略：随机筛选、最高忠实度筛选、最低忠实度筛选，采用两种主流忠实度度量（LExT框架f_m1、自一致性框架f_m2）
- 两组鲁棒性测试：同域NLE随机替换、跨域OOD NLE替换
- 对比基线：零样本、无解释few-shot、零样本CoT

### 关键结果
在6个基准（ECQA、e-SNLI、SNARKS、因果判断、布尔表达式、GSM8K）上测试4个指令微调模型（GPT-4o-mini、Llama3.1-8B、Llama3.3-70B、Mistral-7B-Instruct），结果显示：分类类任务中外部LLM生成的NLE比无解释few-shot平均提效3.2%-22.7%，和人类标注效果相当；自生成NLE经忠实度筛选平均仅提效1%左右，且两种忠实度度量的标注分歧达50%；OOD错配NLE平均导致效果下跌7.5%。

### 核心结论
解释增强ICL的收益核心取决于NLE与样例的语义对齐，而非单纯的忠实度，外部预生成NLE是性价比最高的选型方案。
