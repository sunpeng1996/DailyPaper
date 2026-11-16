---
title: Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles
title_zh: 基于双层集成的大语言模型黑盒不确定性量化方法
authors:
- Wang Ma
- Debarun Bhattacharjya
- Junkyu Lee
- Nhan H Pham
- Harsha Kokel
- Qiang Ji
affiliations:
- Rensselaer Polytechnic Institute
- Lirio
- IBM Software Innovation Lab
- Independent Researcher
arxiv_id: '2611.18453'
url: https://arxiv.org/abs/2611.18453
pdf_url: https://arxiv.org/pdf/2611.18453
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: 大语言模型 · 黑盒不确定性量化
tags:
- Uncertainty Quantification
- Black-box LLM
- Ensemble Learning
- Aleatoric Uncertainty
- Epistemic Uncertainty
one_liner: 通过prompt扰动与随机解码的双层嵌套集成实现黑盒LLM两类不确定性分解
practical_value: '- 电商/搜索/智能客服场景的LLM hallucination检测可直接复用双层集成框架：外层生成query语义不变的paraphrase扰动，内层多次采样解码，通过embedding空间方差拆分AU/EU，AU高触发query澄清，EU高触发RAG/工具调用

  - 1/M偏置修正trick可直接复用，小采样量（M=3~5）下即可得到无偏EU估计，大幅降低闭源LLM调用成本，无需过高采样预算

  - 方法完全不依赖白盒权限，适配对接GPT、Claude等商用闭源大模型的业务场景，无需获取logits或模型参数即可输出不确定性

  - 可基于AU/EU拆分设计分层降级策略：AU高弹出歧义澄清选项，EU高走检索增强链路，TU高直接转人工干预，比单一置信度策略精准度更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM不确定性量化（UQ）方法分为两类：白盒方法需要访问模型logits或参数，大模型场景下计算成本极高且多数商用闭源模型不开放权限；黑盒方法仅能输出单一一致性分数，无法区分偶然不确定性（AU，来自prompt歧义、解码噪声，对应处置策略为query澄清）和认知不确定性（EU，来自模型知识缺口，对应处置策略为检索/工具调用），无法支撑精细化风险控制。
### 方法关键点
1. 双层嵌套集成设计：外层为prompt语义不变扰动集合，通过对原query嵌入加高斯噪声后匹配离线缓存的paraphrase池生成N个语义等价prompt；内层为每个扰动prompt执行M次随机解码，得到多组输出
2. 嵌入空间方差分解：将所有输出映射到句子嵌入空间，通过全协方差定律把总方差拆分为扰动内方差（AU）和扰动间方差（EU）
3. 闭形式偏置修正：针对小M下EU估计的1/M AU泄漏问题，通过简单矩阵减法即可得到无偏EU估计，降低采样成本
### 关键结果
在5个QA基准、4个不同规模/系列的指令微调LLM上测试，AUROC最高达0.845（TriviaQA数据集），性能与白盒方法相当，比现有黑盒基线最高提升0.08 AUROC；相同生成预算下，与SOTA黑盒方法的错误排序性能持平，同时实现AU/EU精准拆分；配对干预实验验证prompt澄清可使AU显著下降3.7%、EU无明显变化，补充知识可使EU显著下降3%、AU无明显变化；长文本事实性检测场景下AU AUROC达0.698，超过SelfCheckGPT等基线0.08以上。
### 核心结论
黑盒场景下仅通过输入语义扰动和输出采样即可实现两类不确定性的精准拆分，完全适配闭源大模型的业务落地需求
