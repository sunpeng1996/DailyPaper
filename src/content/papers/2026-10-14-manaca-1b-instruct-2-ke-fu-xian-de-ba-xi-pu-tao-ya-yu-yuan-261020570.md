---
title: 'Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese
  LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode
  of the LLM Judge'
title_zh: Manacá-1B-Instruct-2：可复现的巴西葡萄牙语原生LLM安全对齐
authors:
- Bruno Leonardo Santos Menezes
- Carlos Leonardo Souza Cardoso
- Fabio André Machado Porto
affiliations:
- National Laboratory for Scientific Computing (LNCC), Brazil
arxiv_id: '2610.20570'
url: https://arxiv.org/abs/2610.20570
pdf_url: https://arxiv.org/pdf/2610.20570
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: LLM安全对齐 · 小语种训练与评测
tags:
- Safety Alignment
- DPO
- SFT
- LLM-as-Judge
- Low-Resource LLM
- Reproducibility
one_liner: 公开小语种LLM安全对齐全流程踩坑，含DPO负结果、SFT最优配比及LLM Judge失效模式
practical_value: '- 做电商Agent、推荐文案生成等场景的LLM安全对齐时，不要盲目信任DPO的训练reward margin，必须用真实自由生成结果验证，避免指标完美但实际行为无变化的静默失效

  - 安全SFT的训练数据配比可参考40%~50%通用数据+50%~60%安全/场景专用数据的区间，平衡安全性和有用性，降低过度拒答率

  - 用LLM-as-Judge做生成内容（如推荐文案、Agent回复）的自动评测时，必须额外统计Judge自身的拒答率，避免有效样本量被静默稀释导致评测结果失真'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
小语种开源LLM的安全对齐普遍缺乏严谨的可复现性记录，负结果通常不公开，LLM-as-Judge评测常被当作黑盒使用，统计显著性验证缺失，巴西葡萄牙语领域相关高质量对齐模型尤其稀缺，现有对齐方法的有效性也缺乏受控实验验证。
### 方法关键点
- 基于1.72B参数的原生巴西葡萄牙语基座Manacá-1B做对齐，先用29.1万条多来源去重指令数据做全参数SFT，3次DPO对齐全部失败后，改用AnswerCarefully风格的Safety-SFT（LoRA参数高效微调）迭代3轮实现安全对齐
- 控制变量扫描Safety-SFT训练集中通用数据的占比（10%~60%），隔离单变量验证配比与安全性、过度拒答率的关系
- 对齐效果评测采用Wilson置信区间、配对McNemar检验经Holm-Bonferroni校正，确保统计显著性，全量公开训练、评测代码及原始数据保证可复现
### 关键实验结果
对比4款同量级巴西葡萄牙语开源LLM，最终v4版本安全拒答率97.2%，95%置信区间下限94.1%高于所有baseline的置信区间上限，过度拒答率仅9.2%与最优baseline持平；发现MT-Bench-PT评测中2个安全类目的LLM Judge会无差别拒答，静默减少33%有效样本量；3次DPO尝试均出现训练reward margin达1.0但实际生成行为无变化的失效情况，Safety-SFT通用数据占比40%~50%为平衡安全性和拒答率的膝点。
### 最值得记住的一句话
做LLM对齐与评测时，不要相信任何没有经过真实生成验证、没有统计显著性支撑的黑盒指标
